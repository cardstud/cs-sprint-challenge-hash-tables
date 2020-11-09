""" One-Way Flight Trip

1. Understand: write a function, 'reconstruct_trip' to reconstruct your trip from your many tickets
    a. Each ticket is represented as a class in the form:

        class Ticket:
            def __init__(self, source, destination):
                self.source = source
                self.destination = destination

    b. 'source' string = starting airport
    c. 'destination' string = the next airport
    d. first flight 'source' = None
    e. final flight 'destination' = None

    f. Input: array of 'Tickets'
            tickets = [
                Ticket{ source: "PIT", destination: "ORD" },
                Ticket{ source: "XNA", destination: "CID" },
                Ticket{ source: "SFO", destination: "BHM" },
                Ticket{ source: "FLG", destination: "XNA" },
                Ticket{ source: "NONE", destination: "LAX" },
                Ticket{ source: "LAX", destination: "SFO" },
                Ticket{ source: "CID", destination: "SLC" },
                Ticket{ source: "ORD", destination: "NONE" },
                Ticket{ source: "SLC", destination: "PIT" },
                Ticket{ source: "BHM", destination: "FLG" }
                    ]
    
    g. Output: an array of strings with the entire route
        ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]

    h. Note: solution should run in linear time

    Test cases
    ----------
    Input:	ticket_1 = Ticket("NONE", "PDX")
            ticket_2 = Ticket("PDX", "DCA")
            ticket_3 = Ticket("DCA", "NONE")

            tickets = [ticket_1, ticket_2, ticket_3]

    Output: ["PDX", "DCA", "NONE"]

2. Plan:
    a. insert tickets into dictionary 
    b. add the first flight
    c. add next flights using i-1 as instructed


3. Execute
"""
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

tickets_dict = {}

def reconstruct_trip(tickets, length):
    route = []

    #insert tickets into dictionary
    for ticket in tickets:
        tickets_dict[ticket.source] = ticket.destination

    #append the first ticket flight
    first_flight = tickets_dict['NONE']
    route.append(first_flight)

    # find the next flight via previous flight's value 
    for i in range(1, len(tickets)):
        route.append(tickets_dict[route[i-1]])

    return route
