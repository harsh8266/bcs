// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
contract PoW {
    struct Block {uint n; bytes32 h;}
    Block[] public chain; uint d = 2;
    function mine(uint nonce) public {
        bytes32 h = keccak256(abi.encodePacked(chain.length, nonce));
        require(valid(h), "fail");
        chain.push(Block(nonce, h));
    }
    function valid(bytes32 h) internal view returns (bool) {
        for (uint i=0; i<d; i++) if (h[i]!=0) return false; return true;
    }
}
