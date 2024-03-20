import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;



public class Main {

    public static BufferedReader br;
    public static StringTokenizer st;
    public static HashMap<Character, Integer> nodeList;



    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        int totalNode = Integer.parseInt(br.readLine());
        Tree tree = new Tree();
        Node[] nodes = new Node[totalNode];
        int nodeData = 65;
        nodeList = new HashMap<>();
        nodeList.put('.', -1);
        //노드 초기화
        for(int i = 0; i < totalNode; i++){
            char tempChar = (char)nodeData;
            nodes[i] = new Node(tempChar);
            nodeList.put(tempChar, i);
            nodeData++;
        }
        //노드 연결 관계 설정
        for(int idx = 0; idx < totalNode; idx++){
            st = new StringTokenizer(br.readLine());
            int rootNode = nodeList.get(st.nextToken().charAt(0));
            int leftNode = nodeList.get(st.nextToken().charAt(0));
            int rightNode = nodeList.get(st.nextToken().charAt(0));
            if(leftNode != -1) {
                tree.setLeft(nodes[rootNode], nodes[leftNode]);
            }
            if(rightNode != -1){
                tree.setRight(nodes[rootNode], nodes[rightNode]);
            }
        }
        tree.preOrder(nodes[0]);
        System.out.println();
        tree.inOrder(nodes[0]);
        System.out.println();
        tree.postOrder(nodes[0]);
    }

    static class Node{
        Object data;
        Node left;
        Node right;

        Node(Object data){
            this.data = data;
            left = null;
            right = null;
        }

    }
    static class Tree{


        public void setLeft(Node node, Node left){
            node.left = left;
        }
        public void setRight(Node node, Node right){
            node.right = right;
        }
        public Node addNode(Object data){
            Node node = new Node(data);
            return node;
        }

        //전위 순회
        public void preOrder(Node node){
            if(node != null){
                System.out.print(node.data);
                preOrder(node.left);
                preOrder(node.right);
            }
        }
        //중위 순회
        public void inOrder(Node node){
            if(node != null){
                inOrder(node.left);
                System.out.print(node.data);
                inOrder(node.right);

            }
        }
        //후위 순회
        public void postOrder(Node node){
            if(node != null) {
                postOrder(node.left);
                postOrder(node.right);
                System.out.print(node.data);
            }
        }
    }

}