import React, { useState, useMemo, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, ReferenceLine, Area } from 'recharts';

// Custom Tooltip Component
const CustomTooltip = ({ active, payload, label, activeDimensions, layers }) => {
  if (!active || !payload || payload.length === 0) return null;

  // Group payload by dimension (combining actual and ideal)
  const dimensionGroups = {};

  payload.forEach(item => {
    // Skip difference and correction layers in tooltip
    if (item.dataKey && (item.name?.includes('Δ ') || item.name?.includes('Target '))) {
      return;
    }

    const dimKey = item.dataKey;
    if (!dimensionGroups[dimKey]) {
      dimensionGroups[dimKey] = { actual: null, ideal: null };
    }

    if (item.name?.includes('(Actual)')) {
      dimensionGroups[dimKey].actual = item.value;
    } else if (item.name?.includes('(Ideal)')) {
      dimensionGroups[dimKey].ideal = item.value;
    }
  });

  return (
    <div style={{
      backgroundColor: '#1e293b',
      border: '1px solid #8b5cf6',
      borderRadius: '8px',
      padding: '12px'
    }}>
      <p style={{ color: '#a78bfa', fontWeight: 'bold', marginBottom: '8px' }}>
        Progress: {typeof label === 'number' ? label.toFixed(0) : label}%
      </p>
      {Object.entries(dimensionGroups).map(([dimKey, values]) => {
        const dim = activeDimensions[dimKey];
        if (!dim) return null;

        const actualVal = values.actual !== null ? values.actual.toFixed(2) : 'N/A';
        const idealVal = values.ideal !== null ? values.ideal.toFixed(2) : 'N/A';

        // Show format: "DimensionName actual/ideal"
        return (
          <p key={dimKey} style={{ color: dim.color, margin: '4px 0', fontSize: '14px' }}>
            {dim.name}: {actualVal}/{idealVal}
          </p>
        );
      })}
    </div>
  );
};

// Custom Legend Component
const CustomLegend = () => {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      gap: '24px',
      paddingTop: '20px',
      fontSize: '14px',
      color: '#fff'
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <div style={{
          width: '30px',
          height: '3px',
          backgroundColor: '#fff',
        }}></div>
        <span>Actual</span>
      </div>
      <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
        <div style={{
          width: '30px',
          height: '2px',
          background: 'repeating-linear-gradient(to right, #fff 0, #fff 5px, transparent 5px, transparent 10px)',
        }}></div>
        <span>Ideal</span>
      </div>
    </div>
  );
};

const App = () => {
  // Analysis mode: 'dimensions' or 'npe'
  const [analysisMode, setAnalysisMode] = useState('dimensions');

  // Data source mode: 'preset' (built-in) or 'loaded' (from JSON)
  const [dataMode, setDataMode] = useState('preset');

  // Loaded story data
  const [loadedData, setLoadedData] = useState(null);
  const [storyMetadata, setStoryMetadata] = useState(null);

  // Layer visibility controls
  const [layers, setLayers] = useState({
    ideal: true,      // Genre ideal curve
    actual: true,     // Actual story data
    difference: false, // Delta between ideal and actual
    correction: false  // Suggested correction trajectory
  });

  const dimensions = {
    intimacy: { name: 'Intimacy', color: '#e91e63', range: [0, 10] },
    powerDiff: { name: 'Power Differential', color: '#ff6f00', range: [-5, 5] },
    infoAsym: { name: 'Info Asymmetry', color: '#ffd600', range: [0, 10] },
    alignment: { name: 'Goal Alignment', color: '#76ff03', range: [0, 10] },
    proximity: { name: 'Physical Proximity', color: '#00e5ff', range: [0, 10] },
    vulnerability: { name: 'Vulnerability', color: '#2979ff', range: [0, 10] },
    desire: { name: 'Desire/Attraction', color: '#d500f9', range: [0, 10] },
    stakes: { name: 'Stakes', color: '#ff1744', range: [0, 10] },
    trust: { name: 'Trust', color: '#00e676', range: [0, 10] },
    danger: { name: 'Danger/Threat', color: '#651fff', range: [0, 10] },
    mystery: { name: 'Mystery/Unknown', color: '#1de9b6', range: [0, 10] },
    self_worth: { name: 'Self-Worth', color: '#8b5cf6', range: [0, 10] },
    goal_alignment: { name: 'Goal Alignment', color: '#10b981', range: [0, 10] },
    info_asymmetry: { name: 'Info Asymmetry', color: '#f59e0b', range: [0, 10] },
  };

  const npeAxes = {
    IA: { name: 'IA (Internal Axis)', color: '#8b5cf6', range: [-1, 1] },
    RA: { name: 'RA (Relational Axis)', color: '#ec4899', range: [0, 180] },
    RA_normalized: { name: 'RA (Normalized)', color: '#ec4899', range: [-1, 1] },
    EA: { name: 'EA (Environmental Axis)', color: '#f59e0b', range: [-1, 1] },
    TA: { name: 'TA (Task Axis)', color: '#10b981', range: [0, 1] },
  };

  // Plot Structures (keeping original from user's code)
  const plotStructures = {
    romancingTheBeat: {
      name: 'Romancing the Beat',
      beats: {
        setup: { name: 'Setup', range: [0, 10], color: '#64748b' },
        meetCute: { name: 'Meet Cute', range: [10, 10], color: '#db2777' },
        noWay: { name: 'No Way', range: [10, 20], color: '#fb923c' },
        connection: { name: 'Connection', range: [20, 50], color: '#4ade80' },
        midpoint: { name: 'Midpoint', range: [50, 50], color: '#c084fc' },
        retreat: { name: 'Retreat', range: [50, 65], color: '#22d3ee' },
        blackMoment: { name: 'Black Moment', range: [65, 75], color: '#b91c1c' },
        epiphany: { name: 'Epiphany', range: [75, 85], color: '#fb7185' },
        grandGesture: { name: 'Grand Gesture', range: [85, 90], color: '#d8b4fe' },
        hea: { name: 'HEA', range: [90, 100], color: '#86efac' },
      }
    },
    heroJourney: {
      name: "Hero's Journey",
      beats: {
        ordinaryWorld: { name: 'Ordinary World', range: [0, 8], color: '#64748b' },
        callToAdventure: { name: 'Call to Adventure', range: [8, 12], color: '#60a5fa' },
        refusalOfCall: { name: 'Refusal of Call', range: [12, 15], color: '#818cf8' },
        meetingMentor: { name: 'Meeting Mentor', range: [15, 20], color: '#c084fc' },
        crossingThreshold: { name: 'Crossing Threshold', range: [20, 25], color: '#d8b4fe' },
        testsAlliesEnemies: { name: 'Tests/Allies/Enemies', range: [25, 50], color: '#4ade80' },
        approachInmostCave: { name: 'Approach Inmost Cave', range: [50, 55], color: '#fb923c' },
        ordeal: { name: 'Ordeal', range: [55, 65], color: '#b91c1c' },
        reward: { name: 'Reward', range: [65, 70], color: '#fcd34d' },
        roadBack: { name: 'Road Back', range: [70, 80], color: '#22d3ee' },
        resurrection: { name: 'Resurrection', range: [80, 90], color: '#f87171' },
        returnWithElixir: { name: 'Return with Elixir', range: [90, 100], color: '#86efac' },
      }
    },
    threeAct: {
      name: 'Three Act Structure',
      beats: {
        setup: { name: 'Act I: Setup', range: [0, 25], color: '#60a5fa' },
        incitingIncident: { name: 'Inciting Incident', range: [10, 15], color: '#c084fc' },
        firstPlotPoint: { name: 'First Plot Point', range: [25, 25], color: '#d8b4fe' },
        risingAction: { name: 'Act II: Rising Action', range: [25, 50], color: '#4ade80' },
        midpoint: { name: 'Midpoint', range: [50, 50], color: '#fb923c' },
        crisis: { name: 'Crisis/Complications', range: [50, 75], color: '#b91c1c' },
        secondPlotPoint: { name: 'Second Plot Point', range: [75, 75], color: '#f87171' },
        climax: { name: 'Act III: Climax', range: [75, 90], color: '#9333ea' },
        resolution: { name: 'Resolution', range: [90, 100], color: '#86efac' },
      }
    },
    mysterySuspense: {
      name: 'Mystery/Suspense Structure',
      beats: {
        ordinaryWorld: { name: 'Ordinary World', range: [0, 8], color: '#64748b' },
        crime: { name: 'Crime/Inciting Incident', range: [8, 12], color: '#b91c1c' },
        initialInvestigation: { name: 'Initial Investigation', range: [12, 25], color: '#60a5fa' },
        firstTwist: { name: 'First Twist', range: [25, 30], color: '#c084fc' },
        deeperInvestigation: { name: 'Deeper Investigation', range: [30, 50], color: '#4ade80' },
        midpointRevelation: { name: 'Midpoint Revelation', range: [50, 55], color: '#fb923c' },
        falseResolution: { name: 'False Resolution', range: [55, 65], color: '#d8b4fe' },
        darkestMoment: { name: 'Darkest Moment', range: [65, 75], color: '#9333ea' },
        finalClues: { name: 'Final Clues', range: [75, 85], color: '#fcd34d' },
        climaxReveal: { name: 'Climax & Reveal', range: [85, 95], color: '#f87171' },
        denouement: { name: 'Denouement', range: [95, 100], color: '#86efac' },
      }
    },
    cozyFantasy: {
      name: 'Cozy Fantasy Arc',
      beats: {
        ordinaryWorld: { name: 'Ordinary World', range: [0, 8], color: '#64748b' },
        disruption: { name: 'Magical Disruption', range: [8, 12], color: '#a78bfa' },
        acceptance: { name: 'Reluctant Acceptance', range: [12, 20], color: '#c084fc' },
        discovery: { name: 'Discovery & Wonder', range: [20, 40], color: '#4ade80' },
        midpoint: { name: 'Midpoint Challenge', range: [40, 50], color: '#fb923c' },
        darkNight: { name: 'Dark Night', range: [50, 70], color: '#b91c1c' },
        transformation: { name: 'Inner Transformation', range: [70, 85], color: '#fb7185' },
        resolution: { name: 'Peaceful Resolution', range: [85, 100], color: '#86efac' },
      }
    },
  };

  // Genre System (keeping from user's code, condensed for brevity)
  const genreSystem = {
    romance: {
      name: 'Romance',
      structure: 'romancingTheBeat',
      subgenres: {
        contemporary: {
          name: 'Contemporary Romance',
          weights: { infoAsym: 0.6, stakes: 0.8, misalignment: 1.0, powerDiff: 0.4, vulnerabilityTrust: 1.2, desireIntimacy: 1.0, proximityTrust: 0.5, danger: 0.3, mystery: 0.4 },
          requirements: { finalIntimacy: [8, 10], finalTrust: [7, 10], finalTension: [0, 3] },
          modifiers: ['Small Town', 'Big City', 'Workplace', 'Second Chance', 'Fake Relationship']
        },
      }
    },
    fantasy: {
      name: 'Fantasy',
      structure: 'heroJourney',
      subgenres: {
        cozyFantasy: {
          name: 'Cozy Fantasy',
          weights: { stakes: 0.8, info_asymmetry: 0.5, misalignment: 1.2, vulnerabilityTrust: 0.8, self_worth: 1.0, goal_alignment: 1.0 },
          requirements: { finalSelfWorth: [7, 10], finalTrust: [7, 10], finalTension: [0, 3] },
          modifiers: ['Magical Library', 'Cottage Core', 'Found Family', 'Slice of Life']
        },
      }
    },
  };

  const [selectedGenre, setSelectedGenre] = useState('romance');
  const [selectedSubgenre, setSelectedSubgenre] = useState('contemporary');
  const [selectedModifier, setSelectedModifier] = useState('');

  const getDefaultVisibleDims = (genre, mode) => {
    if (mode === 'npe') {
      return {
        IA: true,
        RA_normalized: true,
        EA: true,
        TA: true,
        tension: false
      };
    }

    const allDimsFalse = Object.keys(dimensions).reduce((acc, key) => {
      acc[key] = false;
      return acc;
    }, { tension: false });

    const genreSpecific = {
      romance: {
        intimacy: true,
        desire: true,
        vulnerability: true,
        trust: true,
        stakes: true,
        tension: true,
      },
      fantasy: {
        self_worth: true,
        trust: true,
        vulnerability: true,
        stakes: true,
        goal_alignment: true,
        tension: true,
      },
    };

    return { ...allDimsFalse, ...(genreSpecific[genre] || genreSpecific.romance) };
  };

  const [visibleDims, setVisibleDims] = useState(getDefaultVisibleDims('romance', 'dimensions'));

  const currentGenre = genreSystem[selectedGenre];
  const currentSubgenre = currentGenre.subgenres[selectedSubgenre];
  const currentStructure = plotStructures[currentGenre.structure];

  // Load data from query params or localStorage
  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    const dataFile = params.get('data');

    if (dataFile) {
      fetch(dataFile)
        .then(res => res.json())
        .then(data => {
          setLoadedData(data.trajectory || data);
          setStoryMetadata(data.metadata || null);
          setDataMode('loaded');

          // Auto-detect genre if provided
          if (data.metadata?.genre) {
            setSelectedGenre(data.metadata.genre);
          }

          // Auto-set analysis mode if NPE data detected
          if (data.trajectory && data.trajectory[0]?.IA !== undefined) {
            setAnalysisMode('npe');
            setVisibleDims(getDefaultVisibleDims(data.metadata?.genre || 'fantasy', 'npe'));
          }
        })
        .catch(err => console.error('Failed to load data:', err));
    }
  }, []);

  // Preset arcs (Romance example from user's code)
  const presetArcs = {
    romance: [
      { time: 5, beat: 'setup', label: 'Opening Image', intimacy: 0, powerDiff: 0, infoAsym: 2, alignment: 5, proximity: 3, vulnerability: 1, desire: 0, stakes: 2, trust: 3, danger: 1, mystery: 2 },
      { time: 10, beat: 'meetCute', label: 'Meet Cute (Hostile)', intimacy: 1, powerDiff: 0, infoAsym: 3, alignment: 2, proximity: 5, vulnerability: 2, desire: 4, stakes: 3, trust: 1, danger: 2, mystery: 3 },
      { time: 50, beat: 'midpoint', label: 'Midpoint Kiss/Commit', intimacy: 7, powerDiff: 0, infoAsym: 6, alignment: 6, proximity: 10, vulnerability: 8, desire: 8, stakes: 6, trust: 6, danger: 5, mystery: 5 },
      { time: 70, beat: 'blackMoment', label: 'Black Moment', intimacy: 2, powerDiff: -2, infoAsym: 9, alignment: 1, proximity: 2, vulnerability: 9, desire: 9, stakes: 10, trust: 2, danger: 8, mystery: 8 },
      { time: 100, beat: 'hea', label: 'HEA', intimacy: 9, powerDiff: 0, infoAsym: 1, alignment: 9, proximity: 10, vulnerability: 8, desire: 9, stakes: 2, trust: 9, danger: 1, mystery: 1 },
    ],
    fantasy: [
      { time: 5, beat: 'ordinaryWorld', label: 'Ordinary World', self_worth: 2, trust: 5, vulnerability: 2, stakes: 2, goal_alignment: 6, IA: -0.85, RA: 160, EA: 0, TA: 0.1 },
      { time: 50, beat: 'midpoint', label: 'Midpoint Crisis', self_worth: 4, trust: 6, vulnerability: 8, stakes: 10, goal_alignment: 7, IA: -0.4, RA: 90, EA: 0.5, TA: 0.5 },
      { time: 75, beat: 'darkNight', label: 'Dark Night', self_worth: 2, trust: 4, vulnerability: 9, stakes: 10, goal_alignment: 6, IA: -0.9, RA: 120, EA: 0.8, TA: 0.6 },
      { time: 100, beat: 'resolution', label: 'Resolution', self_worth: 9, trust: 9, vulnerability: 5, stakes: 2, goal_alignment: 9, IA: 0.75, RA: 60, EA: -0.2, TA: 1.0 },
    ],
  };

  // Convert loaded trajectory to chart format
  const convertLoadedToChartData = (trajectory) => {
    if (!trajectory || trajectory.length === 0) return [];

    return trajectory.map((point, idx) => {
      const timePercent = ((point.chapter || idx + 1) / trajectory.length) * 100;

      // Normalize RA if in NPE mode
      const chartPoint = {
        time: timePercent,
        label: point.title || `Chapter ${point.chapter || idx + 1}`,
        chapter: point.chapter || idx + 1,
        ...point
      };

      // Add normalized RA for NPE mode
      if (point.RA_orbit !== undefined || point.RA !== undefined) {
        const raValue = point.RA_orbit || point.RA || 180;
        chartPoint.RA_normalized = ((180 - raValue) / 180) * 2 - 1;
      }

      return chartPoint;
    });
  };

  // Get chart data based on mode
  const getChartData = () => {
    if (dataMode === 'loaded' && loadedData) {
      return convertLoadedToChartData(loadedData);
    }

    const arcKey = selectedGenre === 'fantasy' ? 'fantasy' : 'romance';
    return presetArcs[arcKey] || presetArcs.romance;
  };

  // Calculate difference layer
  const calculateDifference = (actual, ideal) => {
    if (!actual || !ideal) return [];

    return actual.map((actualPoint, idx) => {
      const idealPoint = ideal[idx] || ideal[ideal.length - 1];
      const diff = {};

      Object.keys(actualPoint).forEach(key => {
        if (typeof actualPoint[key] === 'number' && typeof idealPoint[key] === 'number') {
          diff[key] = actualPoint[key] - idealPoint[key];
        } else {
          diff[key] = actualPoint[key];
        }
      });

      diff.time = actualPoint.time;
      diff.label = `Δ ${actualPoint.label}`;

      return diff;
    });
  };

  // Calculate correction trajectory
  const calculateCorrection = (actual, ideal) => {
    if (!actual || !ideal) return [];

    // Interpolate from actual to ideal over remaining story time
    return actual.map((actualPoint, idx) => {
      const idealPoint = ideal[idx] || ideal[ideal.length - 1];
      const correction = {};

      // Calculate what the trajectory should be to reach ideal
      const progressRatio = (idx + 1) / actual.length;

      Object.keys(actualPoint).forEach(key => {
        if (typeof actualPoint[key] === 'number' && typeof idealPoint[key] === 'number') {
          // Blend actual and ideal based on progress
          correction[key] = actualPoint[key] + (idealPoint[key] - actualPoint[key]) * progressRatio;
        } else {
          correction[key] = actualPoint[key];
        }
      });

      correction.time = actualPoint.time;
      correction.label = `Target: ${actualPoint.label}`;

      return correction;
    });
  };

  const actualData = getChartData();
  const arcKey = selectedGenre === 'fantasy' ? 'fantasy' : 'romance';
  const idealData = presetArcs[arcKey] || presetArcs.romance;
  const differenceData = calculateDifference(actualData, idealData);
  const correctionData = calculateCorrection(actualData, idealData);

  // Get active dimensions based on mode
  const getActiveDimensions = () => {
    if (analysisMode === 'npe') {
      return npeAxes;
    }
    return dimensions;
  };

  const activeDimensions = getActiveDimensions();

  const toggleDimension = (dim) => {
    setVisibleDims(prev => ({ ...prev, [dim]: !prev[dim] }));
  };

  const toggleLayer = (layer) => {
    setLayers(prev => ({ ...prev, [layer]: !prev[layer] }));
  };

  const switchAnalysisMode = (mode) => {
    setAnalysisMode(mode);
    setVisibleDims(getDefaultVisibleDims(selectedGenre, mode));
  };

  return (
    <div className="w-full min-h-screen bg-gradient-to-br from-slate-900 to-purple-900 text-white p-6">
      <div className="max-w-7xl mx-auto">
        <h1 className="text-4xl font-bold mb-2 text-center">Universal Narrative Physics Engine 🌌</h1>
        <p className="text-purple-200 text-center mb-6 italic">
          Multi-genre story analysis with multi-layer visualization
        </p>

        {/* Mode Controls */}
        <div className="bg-white/10 backdrop-blur rounded-lg p-4 mb-6">
          <div className="grid grid-cols-3 gap-4 mb-4">
            <div>
              <h3 className="text-sm font-bold mb-2 text-purple-300">📊 Analysis Mode</h3>
              <div className="flex gap-2">
                <button
                  onClick={() => switchAnalysisMode('dimensions')}
                  className={`flex-1 px-3 py-2 rounded font-semibold ${
                    analysisMode === 'dimensions'
                      ? 'bg-purple-600'
                      : 'bg-slate-800 hover:bg-slate-700'
                  }`}
                >
                  Dimensions
                </button>
                <button
                  onClick={() => switchAnalysisMode('npe')}
                  className={`flex-1 px-3 py-2 rounded font-semibold ${
                    analysisMode === 'npe'
                      ? 'bg-purple-600'
                      : 'bg-slate-800 hover:bg-slate-700'
                  }`}
                >
                  NPE Axes
                </button>
              </div>
            </div>

            <div>
              <h3 className="text-sm font-bold mb-2 text-purple-300">📚 Data Source</h3>
              <div className="text-sm bg-slate-800 border border-purple-500 rounded px-3 py-2">
                {dataMode === 'loaded'
                  ? `Loaded: ${storyMetadata?.title || 'Custom Data'}`
                  : 'Preset: Genre Examples'}
              </div>
            </div>

            <div>
              <h3 className="text-sm font-bold mb-2 text-purple-300">📖 Genre</h3>
              <select
                value={selectedGenre}
                onChange={(e) => setSelectedGenre(e.target.value)}
                className="w-full bg-slate-800 border border-purple-500 rounded px-3 py-2"
              >
                {Object.entries(genreSystem).map(([key, genre]) => (
                  <option key={key} value={key}>{genre.name}</option>
                ))}
              </select>
            </div>
          </div>

          {/* Layer Controls */}
          <div className="p-3 bg-slate-800/50 rounded">
            <h4 className="text-sm font-semibold mb-2 text-purple-300">🎭 Visualization Layers:</h4>
            <div className="flex flex-wrap gap-3">
              <label className="flex items-center gap-2">
                <input
                  type="checkbox"
                  checked={layers.ideal}
                  onChange={() => toggleLayer('ideal')}
                  className="w-4 h-4"
                />
                <span className="text-sm">Ideal (Genre Curve)</span>
              </label>
              <label className="flex items-center gap-2">
                <input
                  type="checkbox"
                  checked={layers.actual}
                  onChange={() => toggleLayer('actual')}
                  className="w-4 h-4"
                />
                <span className="text-sm font-bold">Actual (Your Story)</span>
              </label>
              <label className="flex items-center gap-2">
                <input
                  type="checkbox"
                  checked={layers.difference}
                  onChange={() => toggleLayer('difference')}
                  className="w-4 h-4"
                />
                <span className="text-sm text-yellow-300">Difference (Δ Gap)</span>
              </label>
              <label className="flex items-center gap-2">
                <input
                  type="checkbox"
                  checked={layers.correction}
                  onChange={() => toggleLayer('correction')}
                  className="w-4 h-4"
                />
                <span className="text-sm text-green-300">Correction (Target Path)</span>
              </label>
            </div>
          </div>
        </div>

        {/* Main Chart */}
        <div className="bg-white/10 backdrop-blur rounded-lg p-6 mb-6">
          <h2 className="text-2xl font-bold mb-4 text-center">
            {analysisMode === 'npe' ? 'NPE Arc Analysis' : 'Dimensional Analysis'}
          </h2>

          <ResponsiveContainer width="100%" height={500}>
            <LineChart margin={{ top: 20, right: 30, left: 20, bottom: 60 }}>
              <CartesianGrid strokeDasharray="3 3" stroke="#ffffff20" />
              <XAxis
                dataKey="time"
                stroke="#fff"
                type="number"
                domain={[0, 100]}
                label={{ value: 'Story Progress (%)', position: 'bottom', offset: 40, fill: '#fff' }}
              />
              <YAxis
                stroke="#fff"
                domain={analysisMode === 'npe' ? [-1, 1] : [0, 10]}
                label={{ value: 'Intensity', angle: -90, position: 'left', offset: 0, fill: '#fff' }}
              />
              <Tooltip
                content={<CustomTooltip activeDimensions={activeDimensions} layers={layers} />}
              />
              <Legend
                wrapperStyle={{ paddingTop: '20px' }}
                content={<CustomLegend />}
              />

              {analysisMode === 'npe' && <ReferenceLine y={0} stroke="#ffffff60" strokeWidth={2} />}

              {/* Ideal Layer */}
              {layers.ideal && Object.entries(activeDimensions).map(([key, dim]) =>
                visibleDims[key] && (
                  <Line
                    key={`ideal-${key}`}
                    data={idealData}
                    type="monotone"
                    dataKey={key}
                    stroke={dim.color}
                    strokeWidth={2}
                    strokeOpacity={0.4}
                    strokeDasharray="5 5"
                    name={`${dim.name} (Ideal)`}
                    dot={false}
                  />
                )
              )}

              {/* Actual Layer */}
              {layers.actual && Object.entries(activeDimensions).map(([key, dim]) =>
                visibleDims[key] && (
                  <Line
                    key={`actual-${key}`}
                    data={actualData}
                    type="monotone"
                    dataKey={key}
                    stroke={dim.color}
                    strokeWidth={3}
                    name={`${dim.name} (Actual)`}
                    dot={{ r: 4 }}
                  />
                )
              )}

              {/* Difference Layer */}
              {layers.difference && Object.entries(activeDimensions).map(([key, dim]) =>
                visibleDims[key] && (
                  <Line
                    key={`diff-${key}`}
                    data={differenceData}
                    type="monotone"
                    dataKey={key}
                    stroke="#fbbf24"
                    strokeWidth={2}
                    name={`Δ ${dim.name}`}
                    dot={false}
                    strokeDasharray="2 2"
                    legendType="none"
                  />
                )
              )}

              {/* Correction Layer */}
              {layers.correction && Object.entries(activeDimensions).map(([key, dim]) =>
                visibleDims[key] && (
                  <Line
                    key={`correction-${key}`}
                    data={correctionData}
                    type="monotone"
                    dataKey={key}
                    stroke="#10b981"
                    strokeWidth={2}
                    strokeOpacity={0.7}
                    name={`Target ${dim.name}`}
                    dot={false}
                    strokeDasharray="8 4"
                    legendType="none"
                  />
                )
              )}
            </LineChart>
          </ResponsiveContainer>
        </div>

        {/* Dimension Controls */}
        <div className="bg-white/10 backdrop-blur rounded-lg p-4 mb-6">
          <h3 className="text-lg font-bold mb-3">
            👁️ Visible {analysisMode === 'npe' ? 'NPE Axes' : 'Dimensions'}
          </h3>

          <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
            {Object.entries(activeDimensions).map(([key, dim]) => (
              <label key={key} className="flex items-center gap-2 p-2 bg-slate-800/50 rounded">
                <input
                  type="checkbox"
                  checked={visibleDims[key]}
                  onChange={() => toggleDimension(key)}
                  className="w-4 h-4"
                />
                <span style={{ color: dim.color }} className="font-semibold text-sm">
                  {dim.name}
                </span>
              </label>
            ))}
          </div>
        </div>

        {/* Info Panel */}
        <div className="bg-white/10 backdrop-blur rounded-lg p-6">
          <h3 className="text-xl font-bold mb-4">📊 Analysis Info</h3>
          <div className="p-4 bg-purple-900/30 rounded border border-purple-500 text-sm space-y-2">
            <p>
              <strong className="text-purple-300">Mode:</strong> {analysisMode === 'npe' ? 'NPE (Narrative Physics Engine)' : 'Dimensional Analysis'}
            </p>
            <p>
              <strong className="text-purple-300">Data:</strong> {dataMode === 'loaded' ? `Loaded from ${storyMetadata?.title || 'file'}` : 'Preset genre examples'}
            </p>
            <p>
              <strong className="text-purple-300">Layers:</strong>{' '}
              {Object.entries(layers).filter(([_, visible]) => visible).map(([layer]) => layer).join(', ')}
            </p>

            {dataMode === 'loaded' && storyMetadata && (
              <>
                <p>
                  <strong className="text-purple-300">Story:</strong> {storyMetadata.title}
                </p>
                <p>
                  <strong className="text-purple-300">Genre:</strong> {storyMetadata.genre}
                </p>
                <p>
                  <strong className="text-purple-300">Chapters:</strong> {loadedData?.length || 0}
                </p>
              </>
            )}

            <div className="border-t border-purple-500/50 pt-3 mt-3 text-xs text-purple-200">
              <p><strong>Layer Guide:</strong></p>
              <ul className="list-disc list-inside space-y-1 mt-1">
                <li><strong>Ideal:</strong> Genre-typical trajectory (dashed lines)</li>
                <li><strong>Actual:</strong> Your story data (solid lines)</li>
                <li><strong>Difference:</strong> Gap between ideal and actual (yellow)</li>
                <li><strong>Correction:</strong> Suggested path to align with genre (green)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default App;
