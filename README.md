# PeopleShip
An experiment in using some blockchain concepts to solve time management issues for flat, self directed, project based organizations

## Background
At USDS we hack the shit out of Github to supplement all kinds of toolsets. Ages ago we started keeping a list of who was assigned to what project in a file called Priorities.md. Being an engineering organization, linters soon followed to make sure any edits to Priorities.md stuck with a consistent format and that individuals were not being overcommitted.   

The linters were soon connected to TravisCI, so that no pull request could be merged that violated Priorities.md. Over time as USDS hired more people, established more teams and took on more projects, editing Priorities.md became harder and harder.   

The process of moving people around, however, began to resemble something that could be better automated through other means. When an engineer wants to shift to another project they contact a variety of different people within USDS with this request. Requests are rarely if ever denied... so essentially these people are just validating these transactions, not approving them. 

## Approach
I'm not 100% sure what this will end up looking like. I've mostly been playing around with the idea of implementing a distribued ledger, which only known members of the organization can validate transactions to. To establish identity I'll probably integrate with some flavor of PKI, perhaps Yubikey to make things easier.

Having PKI also allows a lower difficulty level on proof-of-work (or I suppose eliminating that altogether but that wouldn't be any fun)