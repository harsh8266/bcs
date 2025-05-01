pragma solidity ^0.8.0;
contract PBFT {
    enum P {Idle, Pre, Prep, Com}; uint rid; uint q;
    struct V {address v; P p; bool d;}
    mapping(uint => V[]) public vs; mapping(address => bool) r;
    constructor(address[] memory R, uint _q) {q=_q; for(uint i=0;i<R.length;i++) r[R[i]]=true;}
    modifier onlyR(){require(r[msg.sender]);_;}
    function vote(uint i, P p, bool d) external onlyR {
        vs[i].push(V(msg.sender, p, d));
    }
}
