// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract PBFT {
    enum Phase {Idle, Pre, Prep, Com}

    uint public requestId;
    uint public quorum;

    struct Vote {
        address validator;
        Phase phase;
        bool decision;
    }

    mapping(uint => Vote[]) public votes;
    mapping(address => bool) public isValidator;

    constructor(address[] memory validators, uint _quorum) {
        quorum = _quorum;
        for (uint i = 0; i < validators.length; i++) {
            isValidator[validators[i]] = true;
        }
    }

    modifier onlyValidator() {
        require(isValidator[msg.sender], "Not a validator");
        _;
    }

    function vote(uint _requestId, Phase _phase, bool _decision) external onlyValidator {
        votes[_requestId].push(Vote(msg.sender, _phase, _decision));
    }
}

