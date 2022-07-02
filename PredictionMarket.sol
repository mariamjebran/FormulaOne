//SPDX-License-Identifier: MIT
pragma solidity ^0.8.11;

contract PredictionMarket {
  enum Side { Verstappen, Leclerc, Perez, Russel, Sainz, Other}

  struct Result {
    Side winner;
    Side loser1;
    Side loser2;
    Side loser3;
    Side loser4;
    Side loser5;
  }
  bool public raceFinished;
  Result public result;

  mapping(Side => uint) public bets;
  mapping(address => mapping(Side => uint)) public betsPerGambler;
  address public oracle;

  constructor(address _oracle){
    oracle = _oracle;
  }

  function placeBet(Side _side) external payable {
    require(raceFinished == false, 'race is finished');
    bets[_side] += msg.value;
    betsPerGambler[msg.sender][_side] += msg.value;
  }

  function withdrawGain() external {
    uint gamblerBet = betsPerGambler[msg.sender][result.winner];
    require(gamblerBet > 0, 'you do not have any winning bet');
    require(raceFinished == true, 'race not finished');
    uint gain = gamblerBet + 
                (bets[result.loser1]+bets[result.loser2]+
                 bets[result.loser3]+bets[result.loser4]+
                 bets[result.loser5]) * 
                 gamblerBet / bets[result.winner];
    betsPerGambler[msg.sender][Side.Verstappen] = 0;
    betsPerGambler[msg.sender][Side.Leclerc] = 0;
    betsPerGambler[msg.sender][Side.Perez] = 0;
    betsPerGambler[msg.sender][Side.Russel] = 0;
    betsPerGambler[msg.sender][Side.Sainz] = 0;
    betsPerGambler[msg.sender][Side.Other] = 0;
    // msg.sender.transfer(gain);
    payable(msg.sender).transfer(gain);
  }

  function reportResult(Side _winner, Side _loser1, Side _loser2,
                        Side _loser3, Side _loser4, Side _loser5) 
                        external {
    require(oracle == msg.sender, 'only oracle');
    require(raceFinished == false, 'race is finished');
    result.winner = _winner;
    result.loser1 = _loser1;
    result.loser2 = _loser2;
    result.loser3 = _loser3;
    result.loser4 = _loser4;
    result.loser5 = _loser5;
    raceFinished = true;
  }
  
}