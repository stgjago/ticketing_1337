// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Ticketing {
    uint public ticketCount = 0;

    struct Ticket {
        uint id;
        string buyerName;
        address buyerAddress;
    }

    mapping(uint => Ticket) public tickets;

    event TicketPurchased(uint id, string buyerName, address buyer);

    function buyTicket(string memory _buyerName) public {
        ticketCount++;
        tickets[ticketCount] = Ticket(ticketCount, _buyerName, msg.sender);
        emit TicketPurchased(ticketCount, _buyerName, msg.sender);
    }
}
