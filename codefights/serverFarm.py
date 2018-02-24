"""
Two Sigma engineers process large amounts of data every day, much more than any single server could possibly handle. Their solution is to use collections of servers, or server farms, to handle the massive computational load. Maintaining the server farms can get quite expensive, and because each server farm is simultaneously used by a number of different engineers, making sure that the servers handle their backlogs efficiently is critical.

Your goal is to optimally distribute a list of jobs between servers within the same farm. Since this problem cannot be solved in polynomial time, you want to implement an approximate solution using the Longest Processing Time (LPT) algorithm. This approach sorts the jobs by their associated processing times in descending order and then assigns them to the server that's going to become available next. If two operations have the same processing time the one with the smaller index is listed first. If there are several servers with the same availability time, then the algorithm assigns the job to the server with the smallest index.

Given a list of job processing times, determine how the LPT algorithm will distribute the jobs between the servers within the farm.

Example

For jobs = [15, 30, 15, 5, 10] and servers = 3, the output should be

serverFarm(jobs, servers) = [[1],
                             [0, 4],
                             [2, 3]]
job with index 1 goes to the server with index 0;
job with index 0 goes to server 1;
job with index 2 goes to server 2;
server 1 is going to be available next, since it got the job with the shortest processing time (15). Thus job 4 goes to server 1;
finally, job 3 goes to server 2.
"""

def serverFarm(jobs, servers):
    allocation = [[] for _ in range(servers)]

    def totalTime(serverQ):
        total = 0
        for idx in serverQ:
            total += jobs[idx]
        return total

    if len(jobs) > 0:
        remainingJobs = jobs[:]
        while any([job != -1 for job in remainingJobs]):
            nextJob = max(remainingJobs)
            nextIdx = remainingJobs.index(nextJob)
            targetServer = min(allocation, key=totalTime)
            targetServer.append(nextIdx)
            remainingJobs[nextIdx] = -1
    return allocation
