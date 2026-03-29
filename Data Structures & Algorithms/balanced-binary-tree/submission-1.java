/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    class Balance{
            boolean balanc;
            int minLen;
            int maxLen;
            public Balance(boolean b,int min,int max){
                this.balanc=b;
                this.minLen=min;
                this.maxLen=max;
            }
        };
    public boolean isBalanced(TreeNode root) {
        return balanced(root).balanc;
    }
    public Balance balanced(TreeNode root){
            if (root==null){
                return new Balance(true,0,0);
            }
            if (root.left == null && root.right==null){
                return new Balance(true,1,1);
            }
            Balance l = balanced(root.left);
            Balance r = balanced(root.right);
            if (l.minLen+1<r.maxLen || r.minLen+1<l.maxLen){
                return new Balance(false,0,0);
            }
            return new Balance(l.balanc&&r.balanc,Math.max(r.maxLen,l.maxLen)+1,Math.max(r.maxLen,l.maxLen)+1);
        }
}
