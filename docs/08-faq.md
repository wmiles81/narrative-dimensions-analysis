# Frequently Asked Questions

Common questions about the Narrative Dimensions Analysis system.

## Getting Started

### What is this system?

A physics-inspired approach to story analysis that treats narrative as movement through multidimensional space. Instead of vague advice like "add more tension," it provides precise dimensional configurations that create specific effects.

**Key insight:** Stories are trajectories, not just events. Tension emerges from dimensional configuration.

---

### Do I need to be good at math?

**No.** The system uses simple 0-10 scales and basic addition. If you can score something on a scale of 1-10, you can use this system.

The "physics-inspired" part is conceptual, not mathematical.

---

### Do I have to score every dimension for every scene?

**No.** Focus on the 3-4 dimensions most relevant to your scene. The others can stay static.

**Example:**
In a quiet intimate conversation, you might only track:
- Intimacy
- Vulnerability
- Trust
- Info asymmetry

You don't need to track proximity, power differential, or stakes if they're not moving.

---

### How precise do I need to be?

**Not very.** "Around 5" is fine. What matters is tracking relative changes over time, not absolute perfect scores.

**Example:**
- Intimacy "somewhere between 4 and 6" is fine
- The important part is that it moves from "around 5" to "around 7"
- Direction and magnitude matter more than precision

---

### Can I use this for planning or only revision?

**Both!**

**Planning:** Map intended trajectory before writing
- Chapter 1: intimacy=2, trust=3, desire=5
- Chapter 5: intimacy=4, trust=4, desire=7
- Chapter 10: intimacy=6, trust=3, desire=8
- etc.

**Revision:** Diagnose problems in existing draft
- "Why does Chapter 7 feel flat?" → Check velocity
- "Why doesn't the ending satisfy?" → Check genre requirements

---

## Using the Dimensions

### How do I score [specific situation]?

**General approach:**
1. Read the detailed rubric in `03-dimension-reference.md`
2. Find the closest example
3. If between two levels, you're probably at 5 or 6
4. Trust your instinct

**Common situations:**

**"How do I score intimacy for characters who've known each other for years but aren't close?"**
- They know facts about each other (info asymmetry low)
- But don't share emotional depth (intimacy still low, maybe 3-4)
- Knowing ≠ intimacy

**"How do I score trust in someone reliable but secretive?"**
- Trust in their actions: 7 (reliable)
- Trust overall: 4 (secrets create uncertainty)
- Consider tracking both, or average to 5-6

**"How do I score desire in platonic relationships?"**
- Desire isn't only romantic/sexual
- Can mean "wanting to spend time with"
- For platonic: "How much do they seek each other's company?"

---

### What if my dimensions don't fit the scale?

**Scales are guidelines, not laws.**

If your story has unique needs:
- Add new dimensions (see Advanced Techniques)
- Modify scales (maybe your power scale is -10 to +10)
- Create custom rubrics

The framework adapts to your story.

---

### Can dimensions go backward?

**Absolutely!** That's often where interesting story happens.

**Examples:**
- Trust dropping after betrayal (8 → 2)
- Intimacy retreating after vulnerability rejected (6 → 3)
- Stakes lowering after false victory (9 → 5)

Backward movement creates setbacks, complications, and realistic arcs.

---

### What's the difference between intimacy and trust?

**Intimacy:** How emotionally close you are
- "How much of my inner world do they know?"
- "How deeply connected do we feel?"

**Trust:** How much you believe in their reliability
- "Can I count on them?"
- "Will they do what they say?"

**You can have:**
- High intimacy, low trust (know each other deeply but can't rely on them)
- Low intimacy, high trust (don't know each other well but believe they're reliable)
- Both high (deep bond + security)
- Both low (strangers or enemies)

---

### What's the difference between info asymmetry and mystery?

**Info Asymmetry:** Knowledge gap BETWEEN CHARACTERS
- "What does Character A know that Character B doesn't?"
- Tracked dimension in character interactions

**Mystery:** Knowledge gap between READER and truth
- "What doesn't the reader know yet?"
- Genre-specific dimension for mystery stories

**Example:**
Detective knows the butler did it (info asymmetry between detective and butler = high)
But reader also knows (mystery to reader = low)

---

## Applying to Different Genres

### What if my story doesn't fit a standard genre?

**The system is flexible.**

1. Start with the closest genre template
2. Adjust ending requirements for your needs
3. Modify tension weights
4. Add genre-specific dimensions

See `07-advanced-techniques.md` for creating custom templates.

---

### Can I use this for literary fiction?

**Yes.** Literary fiction still has:
- Character relationships (intimacy, trust)
- Internal conflict (goal alignment with self, power)
- Emotional journeys (vulnerability)

The ending requirements are different (may not resolve cleanly), but the dimensional tracking still applies.

**Adjustment:** Literary fiction may end with:
- Acceptance high (peace with ambiguity)
- Some dimensions unresolved (intentionally)
- Different trajectory patterns (non-traditional arcs)

---

### Can I use this for non-romance genres?

**Absolutely.** The system works for:
- Thriller (danger, stakes, trust)
- Mystery (info asymmetry primary)
- Fantasy (power growth, stakes)
- Horror (fear, danger, vulnerability)
- Literary (internal dimensions)

Romance just has very specific ending requirements. Other genres use the same dimensions differently.

---

### What about comedy?

**Comedy can use dimensional analysis:**

**Comedy often relies on:**
- Info asymmetry (audience knows what character doesn't)
- Goal misalignment (characters at cross purposes)
- Power differential (underdog situations)

**Trajectory pattern:**
- Maintain moderate dimensional chaos
- Resolution brings alignment
- Stakes often personal, not world-ending

---

## Troubleshooting

### My story's trajectory doesn't match the pattern. Is it broken?

**Maybe not!** Patterns are templates, not rules.

**Questions to ask:**
1. Is the different trajectory INTENTIONAL?
2. Does it serve your story's unique needs?
3. Are you meeting your genre's ending requirements?
4. Are dimensional changes earned?

If yes to all, your unique trajectory is fine.

**Red flag:** If the trajectory is different AND you're getting feedback about pacing/believability issues, then dimension analysis can help diagnose.

---

### All my dimensions are at 5. What's wrong?

**"Middle-itis"** - Everything is medium, nothing has contrast.

**Solutions:**
1. Push some dimensions to extremes (2-3 or 7-8)
2. Create gaps (desire=8, proximity=2 creates tension)
3. Vary the dimensions (not all at same level)

**Better configuration:**
```
intimacy: 3 (low)
trust: 5 (medium)
desire: 8 (high)
stakes: 7 (high)
vulnerability: 2 (low, walls up)

Creates contrast and tension
```

---

### My tension calculation seems wrong. It doesn't match how the scene feels.

**Possible reasons:**

**1. Wrong genre weights**
- Using romance weights for thriller scene
- Solution: Use correct genre weights

**2. Missing dimensions in calculation**
- Forgot to include info asymmetry or stakes
- Solution: Include all relevant terms

**3. Your story emphasizes different elements**
- Standard formula doesn't fit your unique story
- Solution: Customize weights (see Advanced Techniques)

**4. Scene has emotional weight not captured dimensionally**
- Prose quality, reader investment, context
- Solution: Dimensions inform tension, but writing quality matters too

---

### How do I handle multiple POV characters?

**Track dimensions from each POV:**

```python
# Chapter 1 (Alice POV)
alice_view = {
    'intimacy_with_bob': 5,
    'trust_in_bob': 6,
    'desire_for_bob': 7
}

# Chapter 2 (Bob POV)
bob_view = {
    'intimacy_with_alice': 5,  # Might match
    'trust_in_alice': 3,       # Might differ!
    'desire_for_alice': 4      # Asymmetric desire = tension
}
```

**The asymmetry creates drama:**
- Alice trusts Bob (6), Bob doesn't trust Alice (3)
- Alice desires Bob (7), Bob less so (4)
- Reader sees both sides

---

### Can I use this for subplot tracking?

**Yes!** See `07-advanced-techniques.md` for multi-subplot tracking.

**Quick version:**
- Use subscripts for different relationships
- Track shared dimensions (stakes, danger) separately
- Focus on 1-2 subplots per chapter

---

## Practical Application

### Do I really need to write all this down?

**Not necessarily.**

**Light touch:** Internalize the concepts, use for diagnosis when stuck
**Medium:** Track key scenes/chapters in spreadsheet
**Heavy:** Full dimensional mapping for entire manuscript

**Use what helps you.** The framework is a tool, not a requirement.

---

### How do I use this with my writing group?

**Shared vocabulary for feedback:**

Instead of: "This scene feels off"
Try: "The intimacy jumped 4 points without a catalyst"

Instead of: "Needs more tension"
Try: "Try increasing the desire-proximity gap or lowering trust"

**Benefits:**
- Specific, actionable feedback
- Less subjective argument
- Clear problems and solutions

---

### Can I use this for querying/pitching?

**Dimensional framing can help pitch:**

**Example pitch with dimensional language:**
"A enemies-to-lovers romance (goal alignment 0 → 10 arc) complicated by a mafia modifier (power differential +4, danger baseline high) where she must overcome a forced proximity situation (proximity locked at 10, captive modifier) to find love."

Translates to: "Enemies-to-lovers mafia romance with forced proximity"

But shows you understand the mechanical elements.

---

### Is this compatible with other story analysis methods?

**Yes!** This integrates with:
- Save the Cat (see Advanced Techniques)
- Hero's Journey (dimensional lens on monomyth)
- Three-Act Structure (dimensional arcs map to acts)
- GMC (Goal = alignment, Motivation = stakes/desire, Conflict = misalignment)
- Character arc frameworks (vulnerability, power growth)

**Dimensional analysis is a lens, not a replacement.**

---

## Philosophy and Approach

### Isn't this too mechanical? What about art?

**The system describes, not prescribes.**

**Mechanical tool for artistic goals:**
- A painter uses color theory (mechanical) to create art
- A musician uses music theory (mechanical) to create art
- A writer can use dimensional analysis (mechanical) to create art

**You still:**
- Choose what to write
- Create characters and prose
- Make artistic decisions

**The system just:**
- Helps diagnose problems
- Suggests configurations for effects
- Provides vocabulary for revision

---

### Does using this make all stories the same?

**No.** Same tools, infinite variations.

**Analogy:**
All music uses the same 12 notes, but infinite songs exist. All paintings use the same color wheel, but infinite artworks exist.

**Your unique story:**
- Your characters
- Your voice
- Your dimensional trajectory
- Your unique configuration choices

The framework doesn't homogenize - it clarifies.

---

### What if I disagree with a genre requirement?

**Then change it!** The requirements are descriptive (what readers expect), not prescriptive (what you must do).

**If you:**
- Write a romance ending at intimacy=6, trust=5
- Intentionally subverting expectations
- Understand reader response might be "not satisfying HEA"

**That's fine.** Just be intentional.

**The system tells you:**
- What typical genre expectations are
- What configuration creates what effect
- What readers will likely feel

**You decide:**
- Whether to meet those expectations
- Whether to subvert them
- How to manage reader response

---

### Can I mix and match from different genres?

**Yes!** See hybrid genres and modifiers.

**Example:**
- Base: Mystery (info asymmetry → 0)
- + Romance (intimacy/trust → high)
- + Paranormal (acceptance of magic)
- + Thriller (danger sustained)

**Must satisfy ALL base genre requirements** for successful hybrid.

---

## Advanced Questions

### How do I handle character growth vs. relationship growth?

**Track both with subscripts:**

```python
# Sarah's individual growth
sarah_individual = {
    'power': -3 → +1 (competence growth)
    'vulnerability': 2 → 7 (walls coming down)
    'acceptance': 3 → 8 (self-acceptance arc)
}

# Sarah's relationship with Jake
sarah_jake = {
    'intimacy': 2 → 8
    'trust': 3 → 7
    'desire': 5 → 9
}

Both arcs matter
```

---

### Can dimensions affect each other?

**Yes!** Some correlate:

**Common correlations:**
- Intimacy often follows vulnerability (when walls down, connection grows)
- Trust often required for vulnerability (feel safe to open up)
- Proximity can accelerate intimacy (forced together, bond faster)

**But not always:**
- Can have intimacy without trust (know each other but unreliable)
- Can have vulnerability without trust (forced exposure)
- Can have proximity without intimacy (stuck together, stay distant)

**Correlations are patterns, not rules.**

---

### How do I represent character flaws dimensionally?

**Flaws affect dimensional patterns:**

**Trust issues:** Character's trust grows slowly, regresses easily
```
Normal: trust 3 → 5 → 7
Flaw: trust 3 → 4 → 2 → 4 → 3 → 5 (jagged, resistant)
```

**Commitment phobia:** Intimacy caps lower, retreats at thresholds
```
Intimacy grows to 6, then drops to 4 (avoidance)
Requires breakthrough to get past 6
```

**Control issues:** Power differential must favor them
```
Uncomfortable when power_diff ≤ 0
Creates conflict when partner gains power
```

---

### What about found family / friendship stories?

**Same dimensions, different context:**

**Friendship uses:**
- Intimacy (emotional closeness)
- Trust (reliability)
- Desire (wanting to spend time together, platonic)
- Vulnerability (opening up)
- Goal alignment (shared purpose)

**Ending requirements different:**
- Not HEA but strong bonds (intimacy ≥ 7, trust ≥ 7)
- Group cohesion (goal alignment among group)
- Individual growth (power, vulnerability arcs)

---

### How do I represent amnesia or identity issues?

**Interesting dimensional configurations:**

**Amnesia:**
```
Pre-amnesia: intimacy=8, trust=8 (married couple)
Post-amnesia: intimacy=1, trust=? (stranger vs. deep body memory)
Info asymmetry: 9 (one knows shared history, other doesn't)

Journey: Re-earning intimacy and trust on new foundation
```

**Secret identity:**
```
Public persona relationship: intimacy=4, trust=6
True self relationship: intimacy=0, trust=0
Info asymmetry: 10 (one identity completely hidden)

Crisis: When identities merge, which relationship survives?
```

---

## Using the Tools

### Which scripts should I use?

**See `scripts/` directory:**

**calculate_tension.py** - For checking if scene has right tension level
**validate_trajectory.py** - For ensuring arc is properly earned
**generate_report.py** - For comprehensive analysis

**Most writers:** Use concepts, not scripts
**Data-oriented writers:** Scripts can help track complex stories

---

### Are there templates or worksheets?

**Not provided, but easy to create:**

**Simple spreadsheet:**
```
Chapter | Intimacy | Trust | Desire | Stakes | Velocity | Notes
1       | 2        | 3     | 5      | 4      | -       | Meet
2       | 3        | 3     | 6      | 5      | 3       | First connection
...
```

**Scene template:**
```
Scene: [Name]
Start State: intimacy=5, trust=6, vulnerability=3
Events: [What happens]
End State: intimacy=6, trust=5, vulnerability=6
Movement: intimacy +1, trust -1, vulnerability +3
Catalyst: Shares childhood trauma (vulnerability jump)
Tension: 6.5
```

---

### How often should I check dimensions?

**Depends on your process:**

**Planner:** Map key scenes before writing
**Pantser:** Check when stuck or in revision
**Hybrid:** Light planning, check every few chapters

**Red flags triggering dimension check:**
- Scene feels flat
- Development feels unearned
- Pacing issues
- Reader feedback about tension/believability

---

## Still Stuck?

### I've read everything and I'm still confused about [X].

**Resources:**

1. **Re-read** `02-core-concepts.md` for theoretical foundation
2. **Check** `03-dimension-reference.md` for scoring help
3. **See** genre guide (`04-genre-guides/`) for your specific genre
4. **Review** `06-diagnostic-guide.md` for your specific problem
5. **Try** working through example in `01-quick-start.md`

**Common confusion points:**

**"I don't understand how tension emerges"**
→ Read tension formula explanation in `02-core-concepts.md`
→ Try calculating tension for a scene you know is tense
→ See which terms contribute most

**"I don't know how to score my scene"**
→ Use `03-dimension-reference.md` detailed rubric
→ Find closest example
→ Remember: precision less important than consistency

**"My genre doesn't fit"**
→ See `07-advanced-techniques.md` for customization
→ Start with closest genre, adjust
→ Create your own template

---

### The system seems overwhelming. Where do I start?

**Minimal viable approach:**

1. **Track just 3 dimensions:** intimacy, trust, stakes
2. **Check velocity:** Are they moving? (avoid static scenes)
3. **Check jumps:** Any ≥ 3 without catalyst? (avoid unearned)
4. **Check ending:** Meet genre requirements?

**That's it.** You can add complexity later.

---

### Can I get personalized help?

This is an open-source analytical framework. For personalized help:
- Writing groups using this system as shared vocabulary
- Beta readers familiar with dimensional analysis
- Critique partners who understand the framework

---

## Philosophy Questions

### Why is this better than traditional story advice?

**Not better, different.**

**Traditional:** "Add more conflict"
**Dimensional:** "Lower goal alignment to 3 and increase power differential to +4"

**Traditional:** "The ending feels flat"
**Dimensional:** "Intimacy is at 6, needs ≥ 8 for romance HEA"

**Benefits:**
- Specific and actionable
- Diagnostic (tells you what's wrong)
- Predictive (tells you what effect configuration will have)

**Limitations:**
- Doesn't replace writing craft
- Can't fix prose quality
- Framework, not magic

---

### Is there research backing this?

**This is a framework, not scientific theory.**

**Based on:**
- Story structure principles (Save the Cat, Hero's Journey)
- Genre conventions (romance HEA requirements, etc.)
- Reader psychology (what creates tension, satisfaction)
- Physics metaphor (phase space, trajectories)

**Not claiming:**
- Scientific truth
- The only way to analyze stories
- Replacement for other methods

**Claiming:**
- Useful lens for analysis
- Diagnostic and predictive power
- Practical tool for revision

---

## Quick Reference

**Most Common Questions:**

Q: Do I need to score everything?
A: No, focus on 3-4 relevant dimensions

Q: How precise?
A: "Around 5" is fine

Q: Can dimensions go backward?
A: Yes! That's where interesting story happens

Q: What if my story doesn't fit a pattern?
A: Patterns are templates, not rules. Adapt as needed.

Q: Is this too mechanical?
A: It's a tool for artistic goals, like color theory for painters

Q: Where do I start?
A: Read `01-quick-start.md` and try scoring one scene

---

**Still have questions?** Review the documentation:
- `01-quick-start.md` - 5-minute intro
- `02-core-concepts.md` - Theory and principles
- `03-dimension-reference.md` - Scoring guide
- `04-genre-guides/` - Genre-specific patterns
- `05-tropes-and-modifiers.md` - Modifiers and their effects
- `06-diagnostic-guide.md` - Problem-solving
- `07-advanced-techniques.md` - Advanced applications
