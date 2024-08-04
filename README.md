
INTRODUCTION:

Inventory management is a crucial aspect of business operations that involves
overseeing the acquisition, storage, and utilization of goods or materials within an
organization. It plays a pivotal role in ensuring a smooth and efficient supply chain,
optimizing costs, and meeting customer demand.
Effective inventory management involves striking a balance between having
enough stock to fulfill customer orders promptly while minimizing excess inventory that
can tie up capital and lead to increased holding costs. The goal is to maintain optimal
inventory levels to meet customer demands, reduce carrying costs, and prevent stock
outs or overstock situations.

OBJECTIVE:

The objective of developing an Inventory Management system is to establish a
streamlined and efficient process for overseeing the acquisition, storage, and
distribution of goods or materials within an organization. This includes achieving the
right balance between maintaining sufficient stock to meet customer demand and
minimizing excess inventory to reduce holding costs.

ABSTRACT:

CASE STUDY:

Description of the situation:

The Kroger Co., a supermarket chain, operates close to 2000 in-store pharmacies
in the United States with a total retail value of about $8 billion. Most pharmacies
typically carry an average of 2500 drugs each. The pharmacies receive the majority of
their drug supplies from Kroger’s warehouses. The rest is shipped from third-party
warehouses.
The pressing issue has been how to manage the enormous drug inventory
problem at the store level. Understocking means frequent shortages with its negative
impact on revenue and customer loyalty, and overstocking leads to tying up capital, high
maintenance cost, and possible drug obsolescence. The goal of good inventory
management at Kroger is to strike a balance between overstocking and understocking.

Inventory policy:

Kroger pharmacy employs the (s, S) periodic review policy that calls for bringing the
inventory level up to S whenever the inventory position (on hand + on order) drops
below the reorder point s. Thus, if at review time the current inventory level is x 16 s2, an
order of size S - x is placed. Otherwise ordering must await the next review process.
Order sizes are rounded up to a multiple of a prespecified package size. Reviews take
place during the review period, normally one or two days before a scheduled delivery.
The ultimate goal of this study is to determine the quantities s and S of the
inventory policy that will minimize the total inventory cost comprising the three
traditional costs of carrying inventory: (1) cost of placing an order, (2) inventory holding
cost, and (3) shortage cost. The developed model must be user-friendly for the
pharmacy personnel in charge of determining the inventory policy for the thousands of
drugs each pharmacy carries.

Each spreadsheet deals with a single drug. Daily demand data (A9:A28) for the drug are
generated randomly from the empirical discrete distribution of approximately one year
of historical data. Column A provides one such (random) scenario using the inverse
sampling method.

This scenario now forms a deterministic equivalence of the empirical demand
distribution. It should remain unaltered throughout subsequent iterative search
comparisons aimed at determining an acceptable inventory policy.
The main input data that drive the simulation are the periodic review values s and S
in(B2:B3). The initial (s, S) values used to start iterative simulations are

Q = Economic order quantity
s = maximum demand of an order period based on historical data
S = s + Q

Ordering policy:
1. On a review day, if (inventory position) 6 s order (S–inventory position), else do not
order.
2. Inventory position reviewed on days MWF.
3. Order is placed at the end of day and remains outstanding throughout lead time.
4. Filled order is received at the end of day.
5. All unfilled demand is backordered (no lost sales).

Simulation formulas (day i):
1. (Beginning inventory)i = (Ending inventory)i-1
2. (Ending inventory)i = (Beginning inventory)i + (Received order)i - (Demand)i
3. (Inventory position)i = (Beginning inventory)i + (On order)i-1
   
Local Search Algorithms:

Step 1. (Fixed Q):
(a) Set s′ = s + I- and S′ = s′ + Q and run the simulation for the new policy 1s′, S′2.
If it yields a lower cost, update 1s, S2 = 1s′, S′2 and repeat (a). Else go to (b).
(b) Set s′ = s - I
+ and S′ = s′ + Q and run the simulation for the new policy
1s′, S′2. If it yields a lower cost, update 1s, S2 = 1s′, S′2 and repeat (a). Else, no
a better solution can be found for fixed Q. Go to Step 2.

Step 2. (Variable Q): Let r = min(I+,I-)
(a) Set S′ = S + r, yielding Q′ = S′ - s 17 Q2, and run the simulation for the new
policy 1s, S′2. If it yields a lower cost, update 1s, S2 = 1s′, S2 and go to step 1(a).
Else go to (b).
(b) Set s′ = s - r, yielding Q′ = S - s′ 16Q2, and run the simulation for the new
policy 1s, S′2. If it yields a lower cost, update 1s, S2 = 1s′, S2 and go to step 1(a).
Else, no better solution can be found for variable Q. Stop.

Conclusion:

The chosen policy helps in reducing shortages and increases revenue.

Tools Used:

Python
