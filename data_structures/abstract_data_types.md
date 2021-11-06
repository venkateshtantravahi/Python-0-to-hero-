<div align='center'>

# Abstract Data Type 

</div>

## Abstract 
The first thing we need to consider while writing any code is the problem. However, the problems that we asked to solve in real life are often complicated. Thus we still need to breakdown such as system down to its fundamental parts and describe these parts in a simple, precise language. This process is called **abstraction**. Through abstraction, we can generate a model of our problem, which defines the abstract view of the problem. Normally the models include the *data* that are affected and the *operations* that are required to access or modify.

As an example, consider a program that manages student records. The head of school comes and asks you to write a program that helps administer to manage students in a class.Well, this is too vague a problem.  We need to think about, for example, what student information is needed for the record?  What tasks should be allowed?

There are many proprties we would think about a student, such as name, DOB, SSN, ID, email, S/o, D/o, transcripts etc. Not all these properties are neccessary to solve our problem. To keep this simple, we assume that student's record includes ID and student's name. The three operation performed by the program includes (1) adding new students (2) searching for existing one (3) dropping student from class. These operations can further explianed as below: 
1. ADD(stu_record) : This operation adds the given student record to the collection of student records.
2. SEARCH (stu_record_id):  This operation searches the collection of student records for the student whose ID has been given.
3. DELETE (stu_record_id):  This operation deletes the student record with the given ID from the collection.

Now, we have modelled our problem in most abstract form : listing the type of data we are intrested in and the operations we are performing on it. But there is no info about how these student records get stored in the memory and how operations gets carried out. This kind of abstraction defined as **abstract data type**.

---
### ADT Definition
An ADT is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them, and the types of parameters of the operations.  An ADT specifies what each operation does, but not how it does it.  Typically, an ADT can be implemented using one of many different data structures.  A useful first step in deciding what data structure to use in a program is to specify an ADT for the program.

In general, the steps of building ADT to data structures are:

- Understand and clarify the nature of the target information unit.
- Identify and determine which data objects and operations to include in the models.
- Express this property somewhat formally so that it can be understood and communicate well.
- Translate this formal specification into proper language.  In Pytohn this becomes Class, C++, this becomes a .h file. In Java, this is called "user interface".
- Upon finalized specification, write necessary implementation.  This includes storage scheme and operational detail.  Operational detail is expressed as separate functions (methods).

---
### Implementation
As we had already defined our ADT for our problem , here we will now have to use some data structures to implement what we have proposed , let's consider two alternatives for above problem: (1) an **unordered list** of records and (3) an **ordered list** of records sorted by IDs. These data structures influences the implementation details such as how fast and efficient our algorithm runs.

First let us look using an **unordered list**. Assume that the student records are stored in an list with no particular order.  We can use a variable n to keep track of the number of students currently in the list (len(list)).
- ADD : simply adds a student to the list. This takes constant amount of time as its independan from length.
- SEARCH :  Since the list is not ordered, we have to scan through the whole list to find the requested record.  The result could be either the record is found or the record doesn't exist.  The time taken to perform the search is proportional to n and the worst case scenario is n.
- DELETE : This operation requires us to first search for the given record.  Once it is found, the algorithm can simply replace it by the last record and decrement n.  Once the record is found, it only takes a constant amount of time to delete it.  But time spent searching for the record is the same as above, proportional to n.  Therefore, in all, this operation also takes time proportional to n, in the worst case.


Now let us consider using an ordered list.  Assume that the student records are sorted in a list, with an increasing order of student IDs.  We can also use a variable n to keep track of the number of students currently in the list.

- ADD:  Since the list is sorted, we first need to find out where should we insert the record.  This can be done by scanning through the list, comparing the current record in the list with the record we want to insert, and finding the smallest index i of the record whose ID is larger than the new ID.  Then the new record should be put to the ith slot in the list.  This operation takes time proportional to n.
- SEARCH:  Since the list of records is sorted by IDs, we can use a binary search to find the given record.  In general, a binary search algorithm first compares the given ID with the ID in the middle of the array (with index n/2 or (n+1)/2).  Then the algorithm branches based on different conditions: if the two IDs are the same, we find the record; if the given ID is smaller, the algorithm continues to search the first half of the current array, ignoring the second half; otherwise, the algorithm continues to search the second half of the current array, ignoring the first half.  The operation time is log2n.
- DELETE:  This operation requires us to first search for the given record.  This can be done in log2n time as shown above.

<div align="center">
    <img src = "https://www.tutorialscan.com/wp-content/uploads/2019/11/Abstract-data-types.jpg"/>
</div>



