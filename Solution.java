import java.util.ArrayList;

/**
 * This class gives the solutions to Problems 1 & 2. You should run this file to see the results.
 *
 * Compiled using
 * java version "1.8.0_72" |  Java(TM) SE Runtime Environment (build 1.8.0_72-b15)
 *
 * Graphnode.java is a class that implements the GNode interface (GNode.java) provided.
 *
 *
 *
 * Sample problem graph used for the test:
 *
 *    A
         B
            E
            F
         C
            G
            H
            I
         D
            J

 Sample answers:
 1) walkGraph(A) = [A, B, E, F, C, G, H, I, D, J]
 2) paths(A) = ( (A B E) (A B F) (A C G) (A C H) (A C I) (A D J) )

 *
 * @author Deji Fajebe
 *
 */
public class Solution {



    public static void main(String[] args) {


        /***************************************************************
         * Use the graph given in the problem as an example:
         ***************************************************************/

        //instantiate the graph nodes
        GraphNode nodeA = new GraphNode("A");
        GraphNode nodeB = new GraphNode("B");
        GraphNode nodeC = new GraphNode("C");
        GraphNode nodeD = new GraphNode("D");
        GraphNode nodeE = new GraphNode("E");
        GraphNode nodeF = new GraphNode("F");
        GraphNode nodeG = new GraphNode("G");
        GraphNode nodeH = new GraphNode("H");
        GraphNode nodeI = new GraphNode("I");
        GraphNode nodeJ = new GraphNode("J");

        //additional node for testing further
        GraphNode nodeX = new GraphNode("X");
        GraphNode nodeY = new GraphNode("Y");


        //set children
        GNode[] children_of_nodeA = new GNode[] {nodeB, nodeC, nodeD};
        nodeA.setChildren(children_of_nodeA);

        GNode[] children_of_nodeB = new GNode[] {nodeE, nodeF};
        nodeB.setChildren(children_of_nodeB);

        GNode[] children_of_nodeC = new GNode[] {nodeG, nodeH, nodeI};
        nodeC.setChildren(children_of_nodeC);

        GNode[] children_of_nodeD = new GNode[] {nodeJ};
        nodeD.setChildren(children_of_nodeD);


//        //additional nodes for testing further
//        GNode[] children_of_nodeE = new GNode[] {nodeX};
//        nodeE.setChildren(children_of_nodeE);
//
//        GNode[] children_of_nodeX = new GNode[] {nodeY};
//        nodeX.setChildren(children_of_nodeX);


        /***************************************************************
         * Problem 1: Get an ArrayList of all nodes present in the graph
         ***************************************************************/

        nodeA.printMsg("\nSolutions to Problems 1 & 2 are provided here.");

        //1a. walk the graph and get the list of all graph nodes
        ArrayList<GNode> resultNodes = nodeA.walkGraph(nodeA);

        nodeA.printMsg("\n1) ArrayList containing every node in the graph are: " + resultNodes);




        /***************************************************************
         * Problem 2: Get an ArrayList of ArrayLists representing all
         * possible paths through the graph starting at 'node'
         ***************************************************************/

        ArrayList<ArrayList<GNode>> arrayListOfPaths = nodeA.paths(nodeA);

        nodeA.printMsg("\n2) The ArrayList of ArrayLists presenting all possible paths are: " + arrayListOfPaths);

    }

}

