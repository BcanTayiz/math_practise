# Pigeon Principle 

simple, idea, very powerful, oddly named

1) Example: there are 5 colors of socks in drawer, how many to gaurentee a mathc ? (6)

**More generally**: n pigeons placed in m pigeonholes with n > m, there must be >= 2 pigeons in same pigeonhole.


**Proof**(by contradiction):
Suppose not. Then,

```math

n = \sum_{holes h}^{} N_{n} \le \sum_{holes h}^{} 1 = m

n > m \\[10px]

we get a contradiction
```

**Lemma**: At a party with n people, there are two people who know the same number of other people.

We could solve this problem with graphs. 

Nodes = people 
edges = ppl know each other 

**Definition** Degree of node is #edges incident to it

**Proof**: the degree of each node 

{0,1,...n-1}

**Lemma**: Given 20 4-digit positive numbers x1,x2 .. xn, then there are two disjoint sets with same sum.

```math
 \exists I,J \subseteq \left\{ 1,2,3..20 \right\} , I,J \neq 0 \\[10px]
 I \cap J \neq \emptyset, \sum_{i \in I}^{x_{i}} = \sum_{i \in J}^{x_{j}}

```

How to prove ? 

pigesons: nonempty subsets
holes: possible sums

```math
n = 2^{20}-1 \\[10px]
n \ge 10^{6} \\[10px]

m \le \sum_{i=1}^{i=20}x_{i} \le 20 \times 10^{4} ,\ 10^{6}\\[10px]

\exists \,\, \text{non empty} A \neq B \\[10px]
\sum_{i \in I}^{x_{i}} - \sum_{i \in J}^{x_{j}}
```

Problem is A & B  need not to be disjoint

```math
I = A \smallsetminus  B\,\, and J =  B \smallsetminus  A \\[10px]

\sum_{i \in A}^{} = \sum_{i \in A \cap B}^{} + \sum_{i \in I}^{} \\[10px]
\sum_{i \in B}^{} = \sum_{i \in A \cap B}^{} + \sum_{i \in J}^{} \\[10px]


```

**Theorem**: In any permutation of integers of 1,2,3 .. nm+1, there is an increasing subsequence of length m + 1 or decreasing subsequence of length n + 1

**Example** m = n = 3
```math
3,2,1,6,5,4,9,8,7,10 \implies 3,6,9,10\,\, \text{is increasing sequence}

```

**Proof**: Consider the sth element in sequence and let 

```math
i_{s} = \text{length of longest incr. subsequence ending sth location}
d_{s} = \text{length of longest decs. subsequence ending sth location}

```
**Claim**:
```math
for \,\, s \neq t,

```

