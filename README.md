# aoc2021
My attempts at solutions to advent of code 2021. You can run each solution by changing into the `code` directory and
running the python file for each day using `python day<num>.py` or `pypy3 day<num>.py`.

Day 19 requires numpy.

Here is a summary of the outputs produced together with the runtime (using Measure-Command on Windows):

| Day | Part 1 solution | Part 2 solution  | Runtime      |
|-----|-----------------|------------------|--------------|
| 1   | 1298            | 1248             | 37ms         |
| 2   | 1962940         | 1813664422       | 37ms         |
| 3   | 3912944         | 4996233          | 41ms         |
| 4   | 28082           | 8224             | 94ms         |
| 5   | 5084            | 17882            | 130ms        |
| 6   | 353079          | 1605400130036    | 37ms         |
| 7   | 344297          | 97164301         | 36ms         |
| 8   | 514             | 1012272          | 41ms         |
| 9   | 554             | 1017792          | 62ms         |
| 10  | 392139          | 4001832844       | 37ms         |
| 11  | 1721            | 298              | 62ms         |
| 12  | 3298            | 93572            | 1500ms       |
| 13  | 638             | CJCKBAPB         | 35ms         |
| 14  | 2223            | 2566282754493    | 40ms         |
| 15  | 390             | 2814             | 4700ms       |
| 16  | 1002            | 1673210814091    | 36ms         |
| 17  | 3916            | 2986             | 242ms        |
| 18  | 3869            | 4671             | 1733ms       |
| 19  | 434             | 11906            | 16000ms      |
| 20  | 5349            | 15806            | 10432ms      |
| 21  | 798147          | 809953813657517  | 149ms        |
| 22  | 611176          | 1201259791805392 | 355ms        |
| 23  | 11332           | 49936            | don't ask    |
| 24  | 59692994994998  | 16181111641521   | done by hand |
| 25  | 334             | -                | 2158ms       |

PC information:
* OS: Windows 10
* CPU: AMD Ryzen 5 3600 (6 cores, 12 threads, 3.6 GHz)
* RAM: 4x8 GB G.Skill RipJaws V DDR4-3200 CL16
* Storage: Samsung EVO 860 m.2 500GB