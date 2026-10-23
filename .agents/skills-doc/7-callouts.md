# Life of a callout

The markup protocol of `feedback-4content` (review and apply modes). The human
steers it by editing the callout label. `check-plan-4content` uses the same notation
for its remarks on a plan: `Should NOT …` drops a remark, `apply` rewrites the plan
and removes all callouts.

```mermaid
stateDiagram-v2
  [*] --> Marked: review mode
  Marked: Should / Must improve, Should shorten
  Marked --> Excluded: the human writes «Should NOT …»
  Marked --> Reserved: the human writes «I should …»
  Marked --> Applied: apply feedback
  Marked --> Clean: the human edits, then remove markup
  Excluded --> Clean: apply drops the callout, text unchanged
  Applied: new ~~old~~
  Applied --> Clean: remove markup keeps new
  Reserved --> Clean: the human edits, then remove all markup

  [*] --> AddCallout: generation or review
  AddCallout: Should add, Must add, AI wrote
  AddCallout --> Clean: only the human, or an explicit request for Should add

  Clean --> [*]
```
