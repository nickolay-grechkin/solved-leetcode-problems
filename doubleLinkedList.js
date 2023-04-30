class ListNode {
    constructor(val, next, prev) {
        this.val = val ?? 0;
        this.next = next ?? null;
        this.prev = prev ?? null;
    }
}

var MyLinkedList = function() {
    this.head = null;
};

/** 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
    if (index < 0 || index >= this.getLength()) return -1;
    let cur = this.head;
    for (let i = 0; i < index; i++) {
        cur = cur.next;
    }
    return cur.val;
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
    if (this.getLength() > 0) {
        let temp = this.head;
        this.head = new ListNode(val);
        this.head.next = temp;
        temp.prev = this.head;
    } else {
        this.head = new ListNode(val);
    }
};

/** 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
    if (this.head == null) {
        this.addAtHead(val);
        return;
    }
    let node = new ListNode(val);
    let cur = this.head;
    while (cur.next !== null) {
        cur = cur.next;
    }

    let temp = cur;
    node.prev = temp;
    temp.next = node;
};

/** 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
    if (index === 0) {
        this.addAtHead(val);
        return
    }
    if (index === this.getLength()) {
        this.addAtTail(val);
        return;
    }
    if (index > this.getLength()) return;
    
    let cur = this.head;
    for (let i = 0; i < index-1; i++) {
        cur = cur.next;
    }
    let node = new ListNode(val);
    node.prev = cur.prev;
    cur.prev.next = node;
    node.next = cur;
    cur.prev = node;
};

/** 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
    if (index < 0 || index >= this.getLength()) return;
    if (index == 0) {
        this.head = this.head.next;
        this.head.next.prev = head;
    }

    let cur = this.head;
    for (let i = 0; i < index-1; i++) {
        cur = cur.next;
    }
    cur.prev.next = cur.next;
    cur.next.prev = cur.prev;
};

MyLinkedList.prototype.getLength = function() {
    let len = 0, cur = this.head;
    while (cur !== null) {
        cur = cur.next;
        len++;
    }
    return len;
};
