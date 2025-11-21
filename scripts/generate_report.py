#!/usr/bin/env python3
"""
Generate comprehensive dimensional analysis reports for stories.
"""

import json
import sys
from typing import Dict, List, Optional
from datetime import datetime

class DimensionalReport:
    def __init__(self, title: str, genre: str, content_level: str):
        """
        Initialize report generator.
        
        Args:
            title: Story/chapter/series title
            genre: Primary genre
            content_level: 'concept', 'chapter', 'book', or 'series'
        """
        self.title = title
        self.genre = genre
        self.content_level = content_level
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def generate_full_report(self,
                            current_state: Dict,
                            trajectory: Optional[List[Dict]] = None,
                            analysis_notes: Optional[str] = None) -> str:
        """Generate comprehensive dimensional analysis report."""

        # Input validation
        if not isinstance(current_state, dict):
            raise TypeError(f"current_state must be a dict, got {type(current_state)}")

        if not current_state:
            raise ValueError("current_state cannot be empty")

        if trajectory is not None:
            if not isinstance(trajectory, list):
                raise TypeError(f"trajectory must be a list, got {type(trajectory)}")
            for i, state in enumerate(trajectory):
                if not isinstance(state, dict):
                    raise TypeError(f"Trajectory state at index {i} must be a dict, got {type(state)}")

        report = []
        report.append("=" * 60)
        report.append(f"DIMENSIONAL NARRATIVE ANALYSIS REPORT")
        report.append("=" * 60)
        report.append(f"Title: {self.title}")
        report.append(f"Genre: {self.genre}")
        report.append(f"Content Level: {self.content_level}")
        report.append(f"Generated: {self.timestamp}")
        report.append("")
        
        # Current State Analysis
        report.append("CURRENT DIMENSIONAL STATE")
        report.append("-" * 40)
        report.extend(self._format_state(current_state))
        report.append("")
        
        # Tension Analysis
        report.append("TENSION ANALYSIS")
        report.append("-" * 40)
        report.extend(self._analyze_tension(current_state))
        report.append("")
        
        # Trajectory Analysis (if provided)
        if trajectory:
            report.append("TRAJECTORY ANALYSIS")
            report.append("-" * 40)
            report.extend(self._analyze_trajectory(trajectory))
            report.append("")
        
        # Diagnostic Assessment
        report.append("DIAGNOSTIC ASSESSMENT")
        report.append("-" * 40)
        report.extend(self._diagnostic_assessment(current_state, trajectory))
        report.append("")
        
        # Recommendations
        report.append("RECOMMENDATIONS")
        report.append("-" * 40)
        report.extend(self._generate_recommendations(current_state, trajectory))
        report.append("")
        
        # Custom Analysis Notes
        if analysis_notes:
            report.append("ADDITIONAL ANALYSIS")
            report.append("-" * 40)
            report.append(analysis_notes)
            report.append("")
        
        report.append("=" * 60)
        report.append("END OF REPORT")
        report.append("=" * 60)
        
        return "\n".join(report)
    
    def _format_state(self, state: Dict) -> List[str]:
        """Format dimensional state for display."""
        lines = []
        
        # Group dimensions by category
        primary = ['intimacy', 'trust', 'desire', 'vulnerability', 'goal_alignment']
        power = ['power_differential', 'info_asymmetry']
        external = ['stakes', 'danger', 'proximity']
        
        lines.append("Primary Relationship Dimensions:")
        for dim in primary:
            if dim in state:
                lines.append(f"  {dim:20} {self._bar_graph(state[dim])} {state[dim]:.1f}/10")
        
        lines.append("\nPower Dynamics:")
        for dim in power:
            if dim in state:
                if dim == 'power_differential':
                    lines.append(f"  {dim:20} {self._power_bar(state[dim])} {state[dim]:+.1f}")
                else:
                    lines.append(f"  {dim:20} {self._bar_graph(state[dim])} {state[dim]:.1f}/10")
        
        lines.append("\nExternal Factors:")
        for dim in external:
            if dim in state:
                lines.append(f"  {dim:20} {self._bar_graph(state[dim])} {state[dim]:.1f}/10")
        
        return lines
    
    def _bar_graph(self, value: float, max_val: float = 10) -> str:
        """Create simple ASCII bar graph."""
        filled = int((value / max_val) * 10)
        return f"[{'█' * filled}{'░' * (10 - filled)}]"
    
    def _power_bar(self, value: float) -> str:
        """Create power differential bar (-5 to +5)."""
        center = 5
        position = int((value + 5) / 10 * 10)
        bar = ['░'] * 11
        bar[center] = '|'
        bar[position] = '█'
        return f"[{''.join(bar)}]"
    
    def _analyze_tension(self, state: Dict) -> List[str]:
        """Analyze tension components."""
        lines = []
        
        # Simplified tension calculation for demo
        tension_components = {
            'Stakes': state.get('stakes', 0) * 0.2,
            'Trust Deficit': max(0, 10 - state.get('trust', 5)) * 0.15,
            'Goal Misalignment': max(0, 10 - state.get('goal_alignment', 5)) * 0.15,
            'Vulnerability Gap': max(0, state.get('vulnerability', 0) - state.get('trust', 0)) * 0.2,
            'Desire-Proximity Gap': max(0, state.get('desire', 0) - state.get('proximity', 5)) * 0.2,
            'Power Imbalance': abs(state.get('power_differential', 0)) * 0.1
        }
        
        total_tension = sum(tension_components.values())
        total_tension = min(10, total_tension)
        
        lines.append(f"Overall Tension: {self._bar_graph(total_tension)} {total_tension:.1f}/10")
        lines.append("\nTension Breakdown:")
        
        sorted_components = sorted(tension_components.items(), key=lambda x: x[1], reverse=True)
        for component, value in sorted_components:
            if value > 0:
                lines.append(f"  {component:20} {value:.2f}")
        
        lines.append(f"\nTension Assessment: {self._tension_label(total_tension)}")
        
        return lines
    
    def _tension_label(self, tension: float) -> str:
        """Get tension level label."""
        if tension < 3:
            return "LOW - Scene may lack engagement"
        elif tension < 5:
            return "MODERATE - Suitable for quieter scenes"
        elif tension < 7:
            return "GOOD - Reader engaged"
        elif tension < 9:
            return "HIGH - Peak tension, use sparingly"
        else:
            return "EXTREME - Maximum tension, reader exhaustion risk"
    
    def _analyze_trajectory(self, trajectory: List[Dict]) -> List[str]:
        """Analyze story trajectory."""
        lines = []
        
        if len(trajectory) < 2:
            lines.append("Insufficient trajectory data for analysis")
            return lines
        
        # Calculate key metrics
        total_movement = 0
        dimensions_tracked = set()
        
        for i in range(1, len(trajectory)):
            for dim in trajectory[i]:
                if dim in trajectory[i-1]:
                    movement = abs(trajectory[i][dim] - trajectory[i-1][dim])
                    total_movement += movement
                    dimensions_tracked.add(dim)
        
        avg_velocity = total_movement / (len(trajectory) - 1) / len(dimensions_tracked) if dimensions_tracked else 0
        
        lines.append(f"Trajectory Points: {len(trajectory)}")
        lines.append(f"Dimensions Tracked: {len(dimensions_tracked)}")
        lines.append(f"Average Velocity: {avg_velocity:.2f} points/chapter")
        
        # Identify key movements
        lines.append("\nKey Dimensional Shifts:")
        first = trajectory[0]
        last = trajectory[-1]
        
        changes = {}
        for dim in first:
            if dim in last:
                change = last[dim] - first[dim]
                if abs(change) >= 1:
                    changes[dim] = change
        
        sorted_changes = sorted(changes.items(), key=lambda x: abs(x[1]), reverse=True)
        for dim, change in sorted_changes[:5]:
            direction = "↑" if change > 0 else "↓"
            lines.append(f"  {dim:20} {direction} {abs(change):.1f} points")
        
        return lines
    
    def _diagnostic_assessment(self, state: Dict, trajectory: Optional[List[Dict]]) -> List[str]:
        """Provide diagnostic assessment."""
        lines = []
        issues = []
        strengths = []
        
        # Check for flat dimensions
        if trajectory and len(trajectory) > 2:
            static_dims = []
            for dim in trajectory[0]:
                if dim in trajectory[-1]:
                    if abs(trajectory[-1][dim] - trajectory[0][dim]) < 1:
                        static_dims.append(dim)
            
            if static_dims:
                issues.append(f"Static dimensions: {', '.join(static_dims)}")
        
        # Check tension balance
        tension_estimate = self._estimate_tension(state)
        if tension_estimate < 3:
            issues.append("Low tension - risk of reader disengagement")
        elif tension_estimate > 8:
            issues.append("Very high tension - cannot sustain for long")
        else:
            strengths.append("Tension level appropriate")
        
        # Check genre requirements
        if self.genre == 'romance':
            if state.get('intimacy', 0) < 3 and state.get('desire', 0) < 3:
                issues.append("Low romance engagement (intimacy & desire both low)")
            if state.get('trust', 10) < 2:
                issues.append("Very low trust - needs rebuilding arc")
        
        # Output assessment
        if strengths:
            lines.append("Strengths:")
            for strength in strengths:
                lines.append(f"  ✓ {strength}")
        
        if issues:
            lines.append("\nPotential Issues:")
            for issue in issues:
                lines.append(f"  ⚠ {issue}")
        
        if not issues and not strengths:
            lines.append("No significant issues detected")
        
        return lines
    
    def _estimate_tension(self, state: Dict) -> float:
        """Quick tension estimate."""
        tension = 0
        tension += state.get('stakes', 0) * 0.2
        tension += max(0, 10 - state.get('trust', 5)) * 0.15
        tension += max(0, state.get('vulnerability', 0) - state.get('trust', 0)) * 0.2
        return min(10, tension)
    
    def _generate_recommendations(self, state: Dict, trajectory: Optional[List[Dict]]) -> List[str]:
        """Generate specific recommendations."""
        lines = []
        recommendations = []
        
        tension = self._estimate_tension(state)
        
        # Tension-based recommendations
        if tension < 3:
            recommendations.append("Increase stakes or introduce conflict")
            recommendations.append("Create information asymmetry between characters")
            recommendations.append("Widen gap between desire and proximity")
        elif tension > 8:
            recommendations.append("Provide moment of relief soon")
            recommendations.append("Resolve at least one tension source")
            recommendations.append("Avoid sustaining this level beyond 1-2 chapters")
        
        # Dimension-specific recommendations
        if state.get('trust', 0) < 3 and state.get('vulnerability', 0) > 6:
            recommendations.append("High vulnerability with low trust creates powerful tension")
        
        if state.get('desire', 0) > 7 and state.get('proximity', 10) < 3:
            recommendations.append("Strong desire with low proximity - perfect for yearning")
        
        if abs(state.get('power_differential', 0)) > 3:
            recommendations.append("Consider power exchange or equalization scene")
        
        # Movement recommendations
        if trajectory and len(trajectory) > 2:
            recent_movement = self._calculate_recent_movement(trajectory)
            if recent_movement < 1:
                recommendations.append("Scene feels static - move 2-3 dimensions")
                recommendations.append("Add catalyst event to justify dimensional shift")
        
        # Genre-specific recommendations
        if self.genre == 'romance' and state.get('intimacy', 0) < state.get('desire', 0) - 3:
            recommendations.append("Large desire-intimacy gap good for slow burn")
        
        # Output recommendations
        if recommendations:
            for i, rec in enumerate(recommendations[:5], 1):
                lines.append(f"{i}. {rec}")
        else:
            lines.append("Story progressing well - maintain current trajectory")
        
        return lines
    
    def _calculate_recent_movement(self, trajectory: List[Dict]) -> float:
        """Calculate recent movement in trajectory."""
        if len(trajectory) < 2:
            return 0
        
        recent = trajectory[-2:]
        total_movement = 0
        dims_counted = 0
        
        for dim in recent[0]:
            if dim in recent[1]:
                total_movement += abs(recent[1][dim] - recent[0][dim])
                dims_counted += 1
        
        return total_movement / dims_counted if dims_counted > 0 else 0

# Example usage
if __name__ == "__main__":
    # Example current state
    current_state = {
        'intimacy': 6,
        'trust': 4,
        'desire': 8,
        'vulnerability': 7,
        'goal_alignment': 5,
        'power_differential': -2,
        'info_asymmetry': 6,
        'stakes': 7,
        'proximity': 3,
        'danger': 5
    }
    
    # Example trajectory (simplified)
    trajectory = [
        {'intimacy': 2, 'trust': 3, 'desire': 4, 'stakes': 5},
        {'intimacy': 3, 'trust': 4, 'desire': 6, 'stakes': 6},
        {'intimacy': 5, 'trust': 5, 'desire': 7, 'stakes': 7},
        {'intimacy': 6, 'trust': 4, 'desire': 8, 'stakes': 7}
    ]
    
    # Generate report
    reporter = DimensionalReport(
        title="Dark Redemption - Chapter 15",
        genre="dark-romance",
        content_level="chapter"
    )
    
    report = reporter.generate_full_report(
        current_state=current_state,
        trajectory=trajectory,
        analysis_notes="Post-betrayal scene. Trust crashed but desire remains high. Perfect setup for groveling arc."
    )
    
    print(report)
