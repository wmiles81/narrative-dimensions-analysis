"""
NPE Genre Constraint Profiles
==============================

The Narrative Physics Engine works across all genres - the axes (IA/RA/EA/TA)
remain the same, but each genre has different physics constraints.
"""

NPE_GENRE_PROFILES = {

    # ========================================================================
    # COZY FANTASY
    # ========================================================================
    'cozy_fantasy': {
        'description': 'Low-stakes, warm, comforting stories with gentle arcs',

        'waveform_constraints': {
            'amplitude': {
                'max': 1.5,
                'ideal': 1.0,
                'note': 'Emotional swings must stay gentle'
            },
            'frequency': {
                'max': 0.3,
                'ideal': 0.15,
                'note': 'Slow, unhurried emotional changes'
            },
            'phase_pattern': 'smooth_ascent',
            'harmonics': 'low_complexity'
        },

        'entropy_constraints': {
            'baseline': 0.1,
            'max_sustained': 0.4,
            'peak_allowed': 0.6,  # Only for dark night
            'resolution_target': 0.05,
            'note': 'Disorder must stay minimal; reader comfort paramount'
        },

        'axis_profiles': {
            'IA': {
                'start_range': (-0.9, -0.5),
                'must_cross_zero': True,
                'final_range': (0.5, 0.9),
                'polarity_flip_timing': (0.75, 0.9),  # Late in story
                'dark_night_depth': -0.95,
                'note': 'Wound → wholeness is central'
            },
            'RA': {
                'orbit_start': (140, 180),
                'orbit_end': (30, 70),
                'closure_rate': 'gradual',
                'regression_allowed': True,
                'max_regression': 40,  # degrees
                'note': 'Relationships deepen slowly and warmly'
            },
            'EA': {
                'baseline': 0.1,
                'spike_max': 1.0,
                'sustained_max': 0.3,
                'note': 'External pressure stays low except crisis'
            },
            'TA': {
                'completion_required': True,
                'final_value': 1.0,
                'failure_allowed': False,
                'note': 'Tasks must complete successfully'
            }
        },

        'threshold_requirements': {
            'dark_night_required': True,
            'dark_night_timing': (0.65, 0.75),
            'polarity_flip_required': True,
            'major_breakthroughs': 2,
            'crisis_convergence': True  # All axes hit low/high simultaneously
        },

        'examples': ['Verity (Library of Haldwick)', 'Legends & Lattes', 'House in the Cerulean Sea']
    },

    # ========================================================================
    # PSYCHOLOGICAL THRILLER
    # ========================================================================
    'psychological_thriller': {
        'description': 'High-tension stories driven by mental games and fear',

        'waveform_constraints': {
            'amplitude': {
                'max': 2.5,
                'ideal': 2.0,
                'note': 'High emotional swings allowed and encouraged'
            },
            'frequency': {
                'max': 0.6,
                'ideal': 0.4,
                'note': 'Rapid oscillations create unease'
            },
            'phase_pattern': 'irregular_spikes',
            'harmonics': 'high_complexity'
        },

        'entropy_constraints': {
            'baseline': 0.5,
            'max_sustained': 0.8,
            'peak_allowed': 1.0,
            'resolution_target': 0.3,  # Can end with lingering unease
            'note': 'High disorder is genre-appropriate'
        },

        'axis_profiles': {
            'IA': {
                'start_range': (-0.7, 0.2),
                'must_cross_zero': False,
                'final_range': (-0.5, 0.8),  # Wide range; can end wounded
                'polarity_flip_timing': (0.5, 1.0),  # Variable
                'dark_night_depth': -0.95,
                'oscillation_pattern': 'erratic',
                'note': 'Protagonist psychological state under constant assault'
            },
            'RA': {
                'orbit_start': (60, 180),
                'orbit_end': (0, 180),  # Can end anywhere
                'closure_rate': 'variable',
                'regression_allowed': True,
                'max_regression': 180,  # Total collapse possible
                'trust_volatility': 'extreme',
                'note': 'Relationships unstable, trust constantly tested'
            },
            'EA': {
                'baseline': 0.6,
                'spike_max': 1.0,
                'sustained_max': 0.9,
                'note': 'Constant external and internal pressure'
            },
            'TA': {
                'completion_required': True,
                'final_value': (0.7, 1.0),
                'failure_allowed': True,  # Pyrrhic victories OK
                'ambiguity_allowed': True,
                'note': 'Resolution may be morally complex'
            }
        },

        'threshold_requirements': {
            'dark_night_required': True,
            'dark_night_timing': (0.7, 0.85),
            'polarity_flip_required': False,
            'major_breakthroughs': 3,
            'false_peaks': True,  # Misleading resolution moments
            'crisis_convergence': True
        },

        'examples': ['Gone Girl', 'Sharp Objects', 'The Silent Patient']
    },

    # ========================================================================
    # DARK ROMANCE
    # ========================================================================
    'dark_romance': {
        'description': 'Morally complex love stories with high stakes and power dynamics',

        'waveform_constraints': {
            'amplitude': {
                'max': 2.0,
                'ideal': 1.7,
                'note': 'Intense emotional swings expected'
            },
            'frequency': {
                'max': 0.5,
                'ideal': 0.3,
                'note': 'Oscillating between conflict and intimacy'
            },
            'phase_pattern': 'power_oscillation',
            'harmonics': 'medium_complexity'
        },

        'entropy_constraints': {
            'baseline': 0.4,
            'max_sustained': 0.7,
            'peak_allowed': 0.95,
            'resolution_target': 0.2,  # Still some edge at end
            'note': 'Sustained tension with explosive moments'
        },

        'axis_profiles': {
            'IA': {
                'start_range': (-0.9, -0.6),
                'must_cross_zero': True,
                'final_range': (0.3, 0.8),
                'polarity_flip_timing': (0.8, 0.95),  # Very late
                'dark_night_depth': -0.95,
                'oscillation_pattern': 'damped',  # Decreasing amplitude over time
                'note': 'Slow burn from wound to acceptance'
            },
            'RA': {
                'orbit_start': (120, 180),
                'orbit_end': (20, 60),
                'closure_rate': 'oscillating',  # Advances and retreats
                'regression_allowed': True,
                'max_regression': 80,
                'power_differential_tracking': True,
                'note': 'Power dynamics drive orbit fluctuations'
            },
            'EA': {
                'baseline': 0.5,
                'spike_max': 1.0,
                'sustained_max': 0.8,
                'moral_ambiguity_required': True,
                'note': 'Stakes stay high; external danger or social pressure'
            },
            'TA': {
                'completion_required': True,
                'final_value': (0.8, 1.0),
                'failure_allowed': False,  # Must achieve HEA/HFN
                'note': 'Must end together despite darkness'
            }
        },

        'threshold_requirements': {
            'dark_night_required': True,
            'dark_night_timing': (0.7, 0.8),
            'polarity_flip_required': True,
            'major_breakthroughs': 3,
            'power_shift_moments': 4,  # Power differential must oscillate
            'crisis_convergence': True
        },

        'examples': ['Captive Prince', 'A Court of Thorns and Roses', 'From Blood and Ash']
    },

    # ========================================================================
    # EPIC FANTASY
    # ========================================================================
    'epic_fantasy': {
        'description': 'Large-scale quest narratives with gradual character transformation',

        'waveform_constraints': {
            'amplitude': {
                'max': 2.0,
                'ideal': 1.5,
                'note': 'Moderate swings; epic scope moderates intensity'
            },
            'frequency': {
                'max': 0.25,
                'ideal': 0.15,
                'note': 'Slow, gradual changes befitting epic scope'
            },
            'phase_pattern': 'heroic_journey',
            'harmonics': 'low_complexity'
        },

        'entropy_constraints': {
            'baseline': 0.3,
            'max_sustained': 0.6,
            'peak_allowed': 0.9,
            'resolution_target': 0.1,
            'note': 'Steady rise to climax, clean resolution'
        },

        'axis_profiles': {
            'IA': {
                'start_range': (-0.8, -0.3),
                'must_cross_zero': True,
                'final_range': (0.6, 1.0),  # True heroic transformation
                'polarity_flip_timing': (0.65, 0.8),
                'dark_night_depth': -0.9,
                'arc_shape': 'gradual_ascent',
                'note': 'Classic hero journey: ordinary → extraordinary'
            },
            'RA': {
                'orbit_start': (100, 160),
                'orbit_end': (30, 80),
                'closure_rate': 'gradual',
                'regression_allowed': True,
                'max_regression': 50,
                'fellowship_dynamics': True,
                'note': 'Bonds forged through shared trials'
            },
            'EA': {
                'baseline': 0.4,
                'spike_max': 1.0,
                'sustained_max': 0.7,
                'world_complexity': 'high',
                'note': 'External stakes escalate with quest progress'
            },
            'TA': {
                'completion_required': True,
                'final_value': 1.0,
                'failure_allowed': False,  # Must defeat Dark Lord
                'bittersweet_allowed': True,  # But at cost
                'note': 'Quest must complete; victory may be costly'
            }
        },

        'threshold_requirements': {
            'dark_night_required': True,
            'dark_night_timing': (0.7, 0.8),
            'polarity_flip_required': True,
            'major_breakthroughs': 4,  # More due to length
            'mentor_death_common': True,
            'crisis_convergence': True
        },

        'examples': ['Lord of the Rings', 'Wheel of Time', 'Stormlight Archive']
    },

    # ========================================================================
    # HORROR (PSYCHOLOGICAL)
    # ========================================================================
    'psychological_horror': {
        'description': 'Fear-driven narratives focused on mental deterioration',

        'waveform_constraints': {
            'amplitude': {
                'max': 2.5,
                'ideal': 2.0,
                'note': 'Extreme emotional swings into terror'
            },
            'frequency': {
                'max': 0.7,
                'ideal': 0.5,
                'note': 'Erratic, unpredictable oscillations'
            },
            'phase_pattern': 'descending_spiral',
            'harmonics': 'chaotic'
        },

        'entropy_constraints': {
            'baseline': 0.6,
            'max_sustained': 0.9,
            'peak_allowed': 1.0,
            'resolution_target': 0.5,  # May not fully resolve
            'note': 'High disorder maintained; unease persists'
        },

        'axis_profiles': {
            'IA': {
                'start_range': (-0.5, 0.2),
                'must_cross_zero': False,
                'final_range': (-1.0, 0.0),  # Can end broken
                'polarity_flip_timing': None,  # May never flip
                'dark_night_depth': -1.0,
                'trajectory': 'descending',  # Gets worse, not better
                'note': 'Protagonist sanity/wholeness deteriorates'
            },
            'RA': {
                'orbit_start': (80, 140),
                'orbit_end': (100, 180),  # Relationships fracture
                'closure_rate': 'diverging',
                'regression_allowed': True,
                'max_regression': 180,
                'isolation_drift': True,
                'note': 'Trust erodes; isolation increases'
            },
            'EA': {
                'baseline': 0.7,
                'spike_max': 1.0,
                'sustained_max': 0.95,
                'fear_primary': True,
                'note': 'Constant fear and vulnerability'
            },
            'TA': {
                'completion_required': False,
                'final_value': (0.0, 0.8),
                'failure_allowed': True,
                'ambiguity_preferred': True,
                'note': 'May end unresolved or with pyrrhic victory'
            }
        },

        'threshold_requirements': {
            'dark_night_required': True,
            'dark_night_timing': (0.8, 0.95),  # Very late
            'polarity_flip_required': False,
            'major_breakthroughs': 1,  # Few moments of hope
            'reality_breakdown_moments': 3,
            'crisis_convergence': True
        },

        'examples': ['House of Leaves', 'The Haunting of Hill House', 'Bird Box']
    },

    # ========================================================================
    # ROMANTIC COMEDY
    # ========================================================================
    'romantic_comedy': {
        'description': 'Light, funny romance with low external stakes',

        'waveform_constraints': {
            'amplitude': {
                'max': 1.3,
                'ideal': 1.0,
                'note': 'Moderate swings; never too intense'
            },
            'frequency': {
                'max': 0.4,
                'ideal': 0.25,
                'note': 'Regular oscillations create comedic rhythm'
            },
            'phase_pattern': 'bouncing_ascent',
            'harmonics': 'low_complexity'
        },

        'entropy_constraints': {
            'baseline': 0.2,
            'max_sustained': 0.4,
            'peak_allowed': 0.6,
            'resolution_target': 0.05,
            'note': 'Low disorder; conflicts are misunderstandings'
        },

        'axis_profiles': {
            'IA': {
                'start_range': (-0.6, -0.3),
                'must_cross_zero': True,
                'final_range': (0.6, 0.9),
                'polarity_flip_timing': (0.8, 0.9),
                'dark_night_depth': -0.7,  # Not too deep
                'note': 'Light insecurity → confidence'
            },
            'RA': {
                'orbit_start': (140, 180),
                'orbit_end': (20, 50),
                'closure_rate': 'bumpy',  # Two steps forward, one back
                'regression_allowed': True,
                'max_regression': 40,
                'banter_dynamic': True,
                'note': 'Proximity increases despite bickering'
            },
            'EA': {
                'baseline': 0.2,
                'spike_max': 0.5,
                'sustained_max': 0.3,
                'stakes_multiplier': 0.7,  # Stakes feel lower
                'note': 'External pressure light and comedic'
            },
            'TA': {
                'completion_required': True,
                'final_value': 1.0,
                'failure_allowed': False,
                'note': 'Must end together and happy'
            }
        },

        'threshold_requirements': {
            'dark_night_required': True,
            'dark_night_timing': (0.75, 0.85),
            'polarity_flip_required': True,
            'major_breakthroughs': 2,
            'comedic_misunderstandings': 4,
            'crisis_convergence': False  # Lighter crisis
        },

        'examples': ['The Hating Game', 'Beach Read', 'Red, White & Royal Blue']
    },

    # ========================================================================
    # MYSTERY (COZY)
    # ========================================================================
    'cozy_mystery': {
        'description': 'Gentle detective stories with community focus',

        'waveform_constraints': {
            'amplitude': {
                'max': 1.2,
                'ideal': 0.9,
                'note': 'Low intensity; puzzle-solving not life-threatening'
            },
            'frequency': {
                'max': 0.3,
                'ideal': 0.2,
                'note': 'Steady pace; clues revealed gradually'
            },
            'phase_pattern': 'mystery_descending',  # Info asymmetry decreases
            'harmonics': 'low_complexity'
        },

        'entropy_constraints': {
            'baseline': 0.3,
            'max_sustained': 0.5,
            'peak_allowed': 0.7,
            'resolution_target': 0.05,
            'note': 'Moderate disorder from mystery; clean resolution'
        },

        'axis_profiles': {
            'IA': {
                'start_range': (-0.5, -0.2),
                'must_cross_zero': True,
                'final_range': (0.4, 0.8),
                'polarity_flip_timing': (0.85, 0.95),
                'dark_night_depth': -0.6,
                'note': 'Self-doubt → competence'
            },
            'RA': {
                'orbit_start': (100, 140),
                'orbit_end': (40, 80),
                'closure_rate': 'gradual',
                'regression_allowed': False,  # Community bonds strengthen
                'note': 'Community trust builds throughout'
            },
            'EA': {
                'baseline': 0.3,
                'spike_max': 0.6,
                'sustained_max': 0.4,
                'info_asymmetry_primary': True,
                'note': 'Pressure from unsolved mystery, not danger'
            },
            'TA': {
                'completion_required': True,
                'final_value': 1.0,
                'failure_allowed': False,
                'note': 'Mystery must be solved'
            }
        },

        'threshold_requirements': {
            'dark_night_required': False,  # Optional
            'dark_night_timing': (0.7, 0.8),
            'polarity_flip_required': True,
            'major_breakthroughs': 3,  # Red herrings, true clues, revelation
            'false_solutions': 2,
            'crisis_convergence': False
        },

        'examples': ['Agatha Raisin', 'Thursday Murder Club', 'Southern Sisters mysteries']
    }
}


# ========================================================================
# GENRE BLENDING RULES
# ========================================================================

GENRE_BLEND_COMPATIBILITY = {
    'cozy_fantasy + romance': {
        'blend_strategy': 'weighted_average',
        'constraint_priority': 'cozy_fantasy',  # Cozy constraints dominate
        'note': 'Romance subplot enhances but doesn\'t override cozy feel'
    },

    'thriller + romance': {
        'blend_strategy': 'max_of_both',  # Take higher constraints
        'constraint_priority': 'equal',
        'note': 'Romantic suspense; both tensions operate'
    },

    'dark_romance + fantasy': {
        'blend_strategy': 'weighted_average',
        'constraint_priority': 'dark_romance',
        'note': 'Fantasy worldbuilding + dark romance dynamics'
    },

    'horror + mystery': {
        'blend_strategy': 'max_of_both',
        'constraint_priority': 'horror',
        'note': 'Mystery structure with horror atmosphere'
    }
}


# ========================================================================
# USAGE EXAMPLES
# ========================================================================

USAGE_GUIDE = """
To apply NPE genre profiles:

1. Select primary genre from NPE_GENRE_PROFILES
2. Check waveform constraints for your trajectory
3. Validate entropy stays within genre bounds
4. Ensure axis progressions match genre patterns
5. Verify threshold timing aligns with genre expectations

Example (Dark Romance):
- IA must oscillate before final polarity flip (late)
- RA orbit must show power dynamics (fluctuating distance)
- EA must stay high (sustained stakes)
- Entropy baseline 0.4, peaks 0.95 allowed
- Waveform amplitude up to 2.0 (intense emotions OK)
"""
