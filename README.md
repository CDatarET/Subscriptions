# Subscriptions
CodeChef Difficulty 504 Problem

Subscriptions
A new TV streaming service was recently launched in Chefland called Chef-TV.

A group of N friends in Chefland wants to subscribe to Chef-TV. Each subscription can be shared by up to 6 people, and the cost of one subscription is X rupees. Your task is to determine the minimum total cost for the group so that everyone can access the service.

Input Format
The first line contains a single integer T — the number of test cases.

Each of the next T lines contains two integers:

N — the number of friends.

X — the cost of one subscription.

Output Format
For each test case, output a single integer — the minimum total cost for the group.

Constraints
1 ≤ T ≤ 1000

1 ≤ N ≤ 100

1 ≤ X ≤ 1000

Sample Input
Copy
Edit
3
1 100
12 250
16 135
Sample Output
Copy
Edit
100
500
405
Explanation
Test Case 1: Only 1 person → needs 1 subscription → Total cost = 1 × 100 = 100

Test Case 2: 12 people → need ceil(12 / 6) = 2 subscriptions → Total cost = 2 × 250 = 500

Test Case 3: 16 people → need ceil(16 / 6) = 3 subscriptions → Total cost = 3 × 135 = 405
