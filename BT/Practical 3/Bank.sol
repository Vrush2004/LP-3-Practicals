//Write a smart contract on a test network. for Bank account of a customer.

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




// SPDX-License-Identifier: MIT: This is a license identifier, which is a standard way to specify the license under which the code is released. Here, it indicates that the contract is licensed under the MIT License.
pragma solidity ^0.8.19;: This line specifies the version of Solidity the code is written for. It ensures that the contract will only compile with Solidity version 0.8.19 or any later version that is backward compatible with it.
contract BankAccount: This defines a new contract named BankAccount. A contract in Solidity is similar to a class in object-oriented programming.
address public owner;: This declares a public state variable owner of type address. It will store the address of the contract owner (the person who deploys the contract).
uint256 public balance;: This declares a public state variable balance of type uint256 (an unsigned integer). It will keep track of the account balance.
event Deposited(address indexed sender, uint256 amount);: This event will be emitted whenever a deposit is made to the contract. It logs the sender's address (sender) and the amount deposited (amount).
event Withdrawn(address indexed receiver, uint256 amount);: This event will be emitted whenever a withdrawal is made. It logs the receiver's address (receiver) and the amount withdrawn (amount).
modifier onlyOwner: A modifier in Solidity is a reusable function that can be applied to other functions to enforce certain conditions.
require(msg.sender == owner, "Only the owner can perform this action.");: The require statement checks if the msg.sender (the address calling the function) is the same as the owner address. If it is not, the transaction is reverted, and the message "Only the owner can perform this action." is shown.
_;: This is a placeholder indicating where the modified function's code will be inserted. The modifier adds this check before executing the actual function.
constructor(): This is the constructor of the contract, which is executed only once when the contract is deployed. It initializes the contract’s state.
owner = msg.sender;: The msg.sender is the address that deployed the contract. This line sets the deployer's address as the owner of the contract.
balance = 0;: Initializes the balance to zero.
function deposit(): A public function that allows anyone to deposit Ether into the contract.
payable: The payable keyword means this function can accept Ether along with the transaction.
require(msg.value > 0, "Deposit amount must be greater than zero.");: This line checks if the amount of Ether sent with the transaction (msg.value) is greater than zero. If it's zero or less, the transaction is reverted with the error message "Deposit amount must be greater than zero."
balance += msg.value;: This increases the balance of the contract by the amount of Ether sent.
emit Deposited(msg.sender, msg.value);: This emits the Deposited event, logging the sender's address (msg.sender) and the deposited amount (msg.value).
function withdraw(uint256 amount): A public function that allows the owner to withdraw a specific amount of Ether from the contract.
onlyOwner: The onlyOwner modifier ensures that only the owner can call this function.
require(amount <= balance, "Insufficient funds.");: This checks if the requested withdrawal amount is less than or equal to the available balance. If not, the transaction is reverted with the message "Insufficient funds."
balance -= amount;: This decreases the contract's balance by the requested withdrawal amount.
payable(msg.sender).transfer(amount);: This sends the specified amount of Ether to the caller's address (msg.sender), which is the owner's address in this case.
emit Withdrawn(msg.sender, amount);: This emits the Withdrawn event, logging the owner's address and the amount withdrawn.