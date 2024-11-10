// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract BankAccount {
    address public owner;
    uint256 public balance;

    // Event to log deposit
    event Deposited(address indexed sender, uint256 amount);
    // Event to log withdrawal
    event Withdrawn(address indexed receiver, uint256 amount);

    // Modifier to ensure that only the owner can withdraw
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Constructor to set the owner of the bank account
    constructor() {
        owner = msg.sender;
        balance = 0;
    }

    // Function to deposit money into the account
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero.");
        balance += msg.value;
        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw money from the account
    function withdraw(uint256 amount) public onlyOwner {
        require(amount <= balance, "Insufficient funds.");
        balance -= amount;
        payable(msg.sender).transfer(amount);
        emit Withdrawn(msg.sender, amount);
    }

}