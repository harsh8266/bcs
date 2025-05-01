pragma solidity ^0.8.0;
contract PoS {
    struct V {uint s; bool a;}
    mapping(address => V) v; address[] pool; address o; uint r=1 ether;
    constructor() {o = msg.sender;}
    function stake() external payable {
        if (!v[msg.sender].a) {v[msg.sender].a=true; pool.push(msg.sender);}
        v[msg.sender].s += msg.value;
    }
    function reward() external { 
        require(msg.sender==o && pool.length>0);
        address w = pool[uint(keccak256(abi.encodePacked(block.timestamp))) % pool.length];
        payable(w).transfer(r);
    }
    function fund() external payable {}
}
