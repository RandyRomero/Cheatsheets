A database index is an additional structure that is derived from the primary data. 

Any kind of index usually slows down writes, because the index also needs to be updated
every time data is written. This is an important trade-off in storage systems: well-chosen indexes speed up read
queries, but every index slows down writes. For this reason, databases don’t usually
index everything by default, but require you—the application developer or database
administrator—to choose indexes manually, using your knowledge of the applica‐
tion’s typical query patterns. You can then choose the indexes that give your applica‐
tion the greatest benefit, without introducing more overhead than necessary
