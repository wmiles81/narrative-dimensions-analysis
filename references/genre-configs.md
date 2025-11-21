# Genre Configurations and Constraints

## Romance Genres

### Contemporary Romance
**Ending Requirements:**
- Intimacy ≥ 8
- Trust ≥ 7
- Goal Alignment ≥ 8
- Power Differential: -1 to 1 (balanced)

**Trajectory Pattern:**
- Steady intimacy climb with 1-2 setbacks
- Trust follows sawtooth pattern (build-break-rebuild)
- Desire high early, dips at 60%, returns for finale

**Key Beats:**
- 25%: First real connection (intimacy jumps 2+ points)
- 50%: False victory (trust peaks temporarily)
- 75%: Black moment (trust crashes, goals misalign)
- 90%: Grand gesture (vulnerability maxed)

### Dark Romance
**Ending Requirements:**
- Intimacy ≥ 7
- Trust ≥ 6
- Power Differential: -2 to 2
- Stakes remain ≥ 5
- Moral Ambiguity accepted

**Trajectory Pattern:**
- Power differential oscillates throughout
- Trust builds VERY slowly
- Stakes never drop below 6
- Danger maintains baseline 4+

**Unique Dynamics:**
- Power exchanges (differential flips sign)
- Trust built through action not words
- Vulnerability forced before chosen
- Desire fights against self-preservation

### Serial Killer Romance
**Ending Requirements:**
- Intimacy ≥ 6
- Trust ≥ 5 (qualified trust)
- Information Asymmetry resolves to ≤ 3
- Moral Ambiguity remains ≥ 7
- Danger never fully resolves

**Trajectory Pattern:**
- Information asymmetry extreme (8+) until 70% mark
- "The reveal" causes dimensional earthquake
- Post-reveal: complete recalibration
- Trust rebuilds on new foundation

**Critical Moments:**
- Discovery scene (info asymmetry crashes)
- Choice point (accept or reject)
- New normal (redefined relationship)

### Enemies to Lovers
**Ending Requirements:**
- Goal Alignment ≥ 8 (complete flip)
- Trust ≥ 7
- Intimacy ≥ 8

**Trajectory Pattern:**
- Goal Alignment slowest dimension
- Desire high despite low trust
- Respect builds before affection
- Power differential neutralizes gradually

**Phases:**
1. Active Opposition (goals opposed, desire denied)
2. Reluctant Alliance (goals align temporarily)
3. Respect Emergence (see beyond surface)
4. Wall Dissolution (vulnerability increases)
5. True Partnership (goals merge)

## Thriller Genres

### Psychological Thriller
**Requirements:**
- Information Asymmetry drives plot
- Trust variable and unreliable
- Stakes escalate continuously
- Reality ambiguity maintained

**Trajectory:**
- Trust wildly fluctuates
- Info asymmetry between characters AND reader
- Stakes compound rather than linear growth
- Power shifts unexpectedly

### Action Thriller
**Requirements:**
- Danger ≥ 7 sustained
- Stakes ≥ 8 sustained
- Physical proximity varies wildly
- Trust builds through shared danger

**Trajectory:**
- Danger spikes and plateaus
- Stakes escalate in discrete jumps
- Proximity forced by circumstances
- Trust earned through action

## Mystery Genres

### Cozy Mystery
**Requirements:**
- Information Asymmetry primary driver
- Stakes moderate (3-6)
- Community trust important
- Danger low (≤ 3)

**Trajectory:**
- Info asymmetry reduces stepwise with clues
- Trust in suspects fluctuates
- Stakes personal not global
- Resolution satisfying and complete

### Noir Mystery
**Requirements:**
- Trust uniformly low (≤ 4)
- Moral Ambiguity high (≥ 7)
- Information costly to obtain
- No clean resolutions

**Trajectory:**
- Trust erodes further
- Every answer raises questions
- Power differential matters
- Cynicism increases

## Fantasy Genres

### Epic Fantasy
**Requirements:**
- Stakes global (≥ 9)
- World Complexity high
- Power differential significant
- Character growth across all dimensions

**Trajectory:**
- Power grows through journey
- Stakes revealed progressively
- Trust builds through trials
- Goal alignment shifts with understanding

### Romantic Fantasy
**Requirements:**
- Magic affects all dimensions
- Destiny/fate as dimension
- World building serves relationship
- Power includes magical and emotional

**Trajectory:**
- Magic amplifies emotional states
- Destiny creates inevitability tension
- Power balanced differently (magic vs emotional)
- Trust includes accepting magical nature

## Hybrid Genres

### Dark Romantic Suspense
Combines:
- Dark romance power dynamics
- Thriller danger levels
- Mystery information patterns

**Critical Balance:**
- Romance arc cannot overshadow suspense
- Danger external AND internal
- Trust issues from both genre sources

### Paranormal Romantic Mystery
Combines:
- Paranormal world rules
- Mystery structure
- Romance arc

**Integration Points:**
- Magic complicates mystery
- Romance stakes include supernatural
- Trust includes accepting otherness

## Constraint Validation Rules

### Universal Rules
1. No dimension can jump ≥ 3 points without catalyst
2. At least 2 dimensions must move per chapter
3. Ending must satisfy ALL genre requirements
4. Black moment must threaten core genre promise

### Genre-Specific Validators

**Romance:** HEA/HFN mandatory
```python
def validate_romance_ending(state):
    return (state.intimacy >= 8 and 
            state.trust >= 7 and 
            state.goal_alignment >= 8)
```

**Thriller:** Danger resolved or accepted
```python
def validate_thriller_ending(state):
    # Either danger is eliminated (≤ 3)
    # OR character has accepted living with unresolved danger (acceptance ≥ 8)
    # Note: acceptance is optional dimension for psychological peace with outcome
    return (state.danger <= 3 or
            state.get('acceptance', 0) >= 8)
```

**Mystery:** Information revealed
```python
def validate_mystery_ending(state):
    return state.info_asymmetry <= 2
```

## Pacing Guidelines by Genre

### Romance Pacing
- Slow burn: Intimacy velocity ≤ 0.5/chapter
- Insta-love: Intimacy velocity ≥ 2/chapter, trust lags
- Standard: 1-1.5 point/chapter on 2-3 dimensions

### Thriller Pacing
- Maintain velocity ≥ 2 on some dimension
- Never static for > 1 chapter
- Danger spikes create urgency

### Mystery Pacing
- Information reveals control pacing
- Red herrings = temporary info asymmetry
- Resolution = rapid cascade

## Common Trajectory Errors

### Romance Errors
- "Unearned HEA": Jump to ending coordinates without journey
- "Third act breakup": Artificial trust crash at 80%
- "Cardboard conflict": Only one dimension creating tension

### Thriller Errors
- "Plateau danger": Constant high stakes = numbness
- "Trust whiplash": Unrealistic trust fluctuations
- "Convenient proximity": Forcing closeness without reason

### Mystery Errors
- "Info dump": Asymmetry resolves too quickly
- "Withholding": Artificial info asymmetry maintenance
- "Unsatisfying reveal": New information at resolution

## Modifier Impacts

### Mafia Modifier
- Power differential baseline +2
- Danger baseline +3
- Stakes include family/loyalty
- Trust complicated by omerta

### Captive Modifier
- Physical proximity forced high
- Power differential extreme
- Stockholm progression possible
- Trust development unique pattern

### Second Chance Modifier
- Start with trust deficit
- Shared history affects all dimensions
- Faster intimacy, slower trust
- Past trauma affects trajectory

## Beat Mapping

Map story beats to dimensional configurations:

### Romance Beat Map
1. Meet: Low all except possibility
2. Attraction: Desire spikes
3. First Connection: Intimacy +2
4. Deepening: Trust building
5. First Conflict: Goal misalignment revealed
6. Retreat: Proximity decreases
7. Pursuit: Vulnerability increases
8. False Victory: Temporary alignment
9. Black Moment: Trust/alignment crash
10. Grand Gesture: Vulnerability maximum
11. Resolution: All dimensions align
12. HEA: Stable high configuration

### Thriller Beat Map
1. Normal World: Low stakes/danger
2. Inciting Incident: Stakes/danger spike
3. Point of No Return: Stakes lock high
4. Rising Danger: Escalating threats
5. False Victory: Temporary safety
6. Reversal: Trust betrayed
7. Dark Night: Maximum danger
8. Final Battle: All dimensions peak
9. Resolution: Danger resolved/accepted

Use these patterns as templates, then customize for specific story needs.
