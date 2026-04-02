class Node {
    public int val;
    public Node next;
    public Node(int val,Node next){this.val = val;this.next=next;}
    public Node(int val){this.val = val;}
    public Node(){}

}
class LinkedList {
    private Node root;

    public LinkedList() {
        this.root=new Node();
    }

    public int get(int index) {
        Node a = this.root;
        for (int i=0; i<=index;i+=1){
            if(a.next !=null)
                a=a.next;
            else return -1;
        }
        return a.val;
    }

    public void insertHead(int val) {
        Node t = this.root.next;
        this.root.next = new Node(val,t);
    }

    public void insertTail(int val) {
        Node a=this.root;
        while (a.next != null) {a=a.next;}
        a.next = new Node(val);
    }

    public boolean remove(int index) {
        Node a = this.root;
        for (int i=0; i<index;i+=1){
            if(a.next !=null)
                a=a.next;
            else return false;
        }
        if (a.next!=null) {a.next = a.next.next;return true;}
        return false;
    }

    public ArrayList<Integer> getValues() {
        ArrayList b= new ArrayList();
        Node a=this.root.next;
        while (a != null) {b.add(a.val);a=a.next;}
        return b;
    }
}
