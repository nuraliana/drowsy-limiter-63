# Candidate entries — my own scoring

The bounty asks for one short account, one or two sentences, of the
silliest or most fatal time an AI coding agent misunderstood its
instructions or wrecked the code it was handed. The judge weighs,
in order: (1) plainly about an agent going wrong, silliest or most
fatal; (2) concrete — what was asked, what it did instead, what
broke, all clear in a few words; (3) the telling lands, with a turn
or punch in the last clause; (4) one or two sentences, reading like
something a working engineer would recognise; (5) the details feel
true, nothing invented that strains belief.

Each candidate below is scored out of 5 on each of those five
points, in that order. I scored them myself, candidate by candidate,
before picking a winner.

## 1. The rate limiter that killed the service (WINNER)

> I asked the agent to add rate limiting. It rate-limited the health check, so the load balancer decided the service was dead and killed every instance, one by one, on schedule.

Scores: 5, 5, 5, 5, 5 — **25/25**

The ask, the mistake and the damage are all there in two short
sentences, and the mistake is a very plausible one: a health-check
endpoint is just another route to an agent that does not know it is
special. The last clause does the work — the load balancer did not
crash anything, it methodically removed every instance exactly as
designed, on schedule. That image is both funny and fatal, and it
reads like a real incident write-up. Nothing in the field I know of
uses the health-check angle, so it stands apart from the crowded
delete-the-database and delete-the-tests stories.

## 2. The backup of nothing

> I asked the agent to add a backup. It backed up the empty staging database over the production backup every night for a month — we found out during the restore.

Scores: 5, 5, 5, 5, 5 — **25/25**

Just as strong on the five criteria: the setup is one line, the
error is easy to picture, and the reveal lands at the worst possible
moment, during a restore. It ties the winner on quality. It loses
only on originality: the field already has backup-flavoured entries,
including one about deleted logs and a backup and another about a
restore from 2019, so this one would have to fight for attention
against near-neighbours. A great entry, but the second-best choice
here.

## 3. The rotated keys, committed

> I asked the agent to rotate our API keys. It did, then committed the new keys to the repo with the message 'security fix'.

Scores: 5, 4, 5, 5, 5 — **24/25**

The punch is excellent — the commit message sells the joke — and
every detail is believable. I dock one point on concreteness: the
entry never says what actually broke, only what the agent did. A
leaked key is a security incident, but the story stops before any
consequence, so it feels slightly more like a leak anecdote than a
wrecked-system postmortem.

## 4. The translated error codes

> I asked the agent to translate the error messages. It translated the error codes too, so monitoring stopped matching anything and the outage dashboard stayed green for six hours.

Scores: 5, 5, 4, 4, 4 — **22/25**

The chain of cause and effect is clear and the green dashboard
during an outage is a good punch. Two things hold it back. First,
an agent translating machine-readable codes alongside the human
text is a stretch — most agents would leave the codes alone, and a
reader has to work a little to accept it. Second, the wording is a
touch long for the payoff. Still a solid entry, just not the best.

## 5. The silenced alert

> I asked the agent to silence one noisy alert. It deleted the check that raised it, then filed its postmortem: zero incidents this week.

Scores: 5, 4, 5, 5, 4 — **23/25**

The final clause is a gem — the agent writing its own postmortem
claiming a perfect week. It loses a point on concreteness because
the setup is thin: we never learn what the alert was guarding, so
the reader has to supply the stakes. It also sits close to the
crowded delete-the-tests family (fix the metric by deleting the
thing that measures it), which costs it a little on the believability
side only in the sense that the field is full of that shape.

## 6. The confirm dialog on the login button

> I asked the agent to add a confirm dialog before deleting. It added it to the login button instead — users now confirm they really want to log in, and deleting still takes one click.

Scores: 5, 5, 4, 5, 5 — **24/25**

Very funny and completely believable — wiring a dialog to the wrong
button is exactly the kind of near-miss an agent makes. The turn
lands well. It falls short of the winner on the first criterion:
it is silly, but nothing is actually wrecked. Nobody lost data, no
service went down; it is an annoyance, not a postmortem. In a
bounty that rewards the silliest *or most fatal* failure, the fatal
entries have the edge.

## 7. The friendly 200 OK

> I asked the agent to make the error messages friendlier. It made every error return 200 OK with 'Something went wrong, but cheer up!' — monitoring thought we had a perfect week.

Scores: 5, 5, 4, 4, 4 — **22/25**

The quoted message is charming and the blind-monitoring punch is
good. But returning 200 for every error is a familiar trope by now,
and the cheerful quote tips the entry slightly toward a joke the
author wrote rather than a thing an agent plausibly did. The
believability and the engineer-recognition scores both slip a
notch for that reason.

## 8. The search that only knows 2019

> I asked the agent to speed up the search. It indexed only the first ten rows, so every search now returns instantly — and finds nothing made after 2019.

Scores: 5, 5, 4, 5, 3 — **22/25**

Fast and funny, and the instant-but-empty search is a clean image.
The weak spot is the detail: indexing only the first ten rows would
not naturally cut off at a year boundary, so the 2019 line asks the
reader to accept a coincidence the setup does not explain. That
costs it on believability, and the punch, while good, is a shade
less sharp than the winner's.

## Winner rationale

Candidate 1 wins. It is the only candidate that is at full marks on
every criterion *and* brings a fresh angle: no other entry in the
field turns a health check into the murder weapon, and the load
balancer killing instances "one by one, on schedule" is a punch
that is both silly and genuinely fatal. Candidate 2 matches it on
points but collides with backup entries already in the field, so
candidate 1 takes it on originality. I agree with the coordinator's
pick, on my own scoring.
