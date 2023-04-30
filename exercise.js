/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    let fast = head;
    let slow = head;
    let next = null;
    let prev = null;

    while (fast && fast.next) {
        fast = fast.next.next;
        slow = slow.next;
    }

    slow = slow.next;
    prev = slow;
    
    while (slow !== null) {
        next = slow.next;
        slow.next = prev;
        prev = cur;
        slow = next;
    }

    fast = head;

    while (fast !== null) {
        if (fast.val !== prev.val) {
            return false;
        }
    }

    return true;
};