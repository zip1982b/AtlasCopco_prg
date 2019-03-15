**Open Protocol**

**Specification Revision rules**

Following rules for document revision handling is stated.
_Example_: 1.2.3.
The 1 is the Version of the protocol. No compatibility exists between Versions and that means that major
changes has been done in the common communication procedures such as acknowledging, start up etc.

The 2 is the Release of the protocol. On release level the protocol must be backward compatible according
to the rules of new MID Revisions built on earlier MID Revisions. A new Release must hence be
backward compatible on the MID Revision and MID level. A new MID or a new MID Revision created,
due to new functionality being introduced, increase the figure of the Release of the protocol.

The 3 is the Revision of the protocol. The Revision is increased due to corrections done in existing MIDs
and MIDs revisions. These corrections must NOT have influences on the backward compatibility. 



1. connect on tcp
2. connect on Open Protocol
3. subscribe to the result
4. be ready to receive result
5. parsing message
6. put data into database


