# The files in the folder are the solutions to the given challenge problems:

1. Given the interface "GNode" (in **GNode.java**) that looks like this:

   public interface GNode {
     public String getName();
    public GNode[] getChildren();
   }
  Implement a function with the following signature:

       public ArrayList walkGraph(GNode);

   which should return a ArrayList containing every GNode in the
   graph. Each node should appear in the ArrayList exactly once
   (i.e. no duplicates).

   * Observe that this GNode can be thought of as defining a graph.
   * In implementing the functions below, you can assume that any
   * graph defined by a GNode is acyclic (no cycles).
   * Assume that when a GNode has no children, getChildren() returns
   * a array of size 0, and *not* null.
   * You can also assume that all children returned by getChildren()
   * are not null.

2. Implement a function with the following signature:

        public ArrayList paths(GNode node);

   which should return a ArrayList of ArrayLists, representing all
   possible paths through the graph starting at 'node'. The ArrayList
   returned can be thought of as a ArrayList of paths, where each path
   is represented as an ArrayList of GNodes.
   
   ** The two functions for both problem 1 and 2 are implemented in GraphNode.java. To test the solution, run the
   solution file, **Solution.java** to see results.

3. **count-words-in-txt-file.py** is a quick and dirty Python program to produce a count of all the different
   "words" in a text file. To use this file, put the script in the same folder or path as the target input file
   and run it from the command line. The input file must be a .txt file in ASCII.
   
   The output look like this:

    Word Count
    like	6
    what	6
    a	6
    about	5
    big	2
    words	2
    home	2
    girl	2
    special	2
    300	2
    boy	2
    of	2
    makes	2
