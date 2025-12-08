from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Digital Electronics: Sequential Circuits Q&A', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_body(self, questions):
        self.set_font('Arial', '', 12)
        for q_num, (question, answer) in enumerate(questions, 1):
            # Question
            self.set_font('Arial', 'B', 12)
            self.multi_cell(0, 7, f"{q_num}. {question}")
            # Answer
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 7, f"Answer: {answer}")
            self.ln(3) # Space between questions

# Data: The Questions and Answers
qa_data = [
    ("What is a sequential circuit?", 
     "A sequential circuit is a digital logic circuit where the output depends not only on the present inputs but also on the history of past inputs (the current state). Unlike combinational circuits, sequential circuits possess memory elements."),
    ("Write the names of any two basic forms of memory element.", 
     "1. Latches\n2. Flip-flops"),
    ("What is the main difference between latches and flip flops?", 
     "Latches are level-triggered (output changes when enable is active), whereas Flip-flops are edge-triggered (output changes only at a specific clock transition)."),
    ("What will be the output (Q) of J-K flip-flop when input J = 0 & K = 0?", 
     "The output remains unchanged (Hold State). Q(n+1) = Q(n)."),
    ("In a T flip-flop, output (Q) changed from 1 to 0. What was the logic level applied at the input terminal T?", 
     "The logic level was 1 (Toggle mode)."),
    ("What is asynchronous sequential circuit?", 
     "An asynchronous sequential circuit is a system without a global clock. State changes occur immediately when input signals change, governed only by propagation delays."),
    ("What will be the output (Q) of S-R flip-flop when input S = 1 & R = 1?", 
     "The output is Invalid (Indeterminate). This state is forbidden as it tries to set and reset simultaneously."),
    ("How many bits a flip-flop can store?", 
     "A single flip-flop can store 1 bit of data."),
    ("How a PISO register is different from SIPO register?", 
     "PISO (Parallel-In Serial-Out) loads data simultaneously and shifts it out bit-by-bit. SIPO (Serial-In Parallel-Out) takes data in bit-by-bit and outputs it all simultaneously."),
    ("Write any two applications of shift registers.", 
     "1. Serial-to-Parallel/Parallel-to-Serial data conversion.\n2. Producing time delays."),
    ("What is meant by triggering of Flip flop?", 
     "Triggering refers to the signal event (like a Rising Edge or Falling Edge of a clock) that causes the flip-flop to change its state."),
    ("Draw and explain SR latch.", 
     "An SR latch is a basic memory element made of cross-coupled NOR or NAND gates. It has a Set state (S=1, R=0), Reset state (S=0, R=1), and Hold state (S=0, R=0)."),
    ("Explain the differences between JK Flip flop and Master Slave Flipflop.", 
     "A standard JK Flip-flop suffers from the 'Race Around Condition' if the clock is too wide. A Master-Slave Flip-flop uses two cascaded latches to isolate input from output, eliminating the Race Around Condition."),
    ("What do you understand by transparent latch?", 
     "A transparent latch (usually D-Latch) is one where the output follows the input exactly while the Enable signal is high. It becomes 'transparent' to the data."),
    ("What is race around condition in JK flip flops.", 
     "It occurs when J=1, K=1 and the clock pulse is longer than the propagation delay. The output toggles multiple times within one clock pulse, causing uncertainty."),
    ("What is the problem with SR flip flop and how it can be removed in JK flip flop.", 
     "Problem: SR flip-flop has an invalid state when S=1, R=1. Solution: The JK flip-flop uses feedback to toggle the output when J=1, K=1, removing the invalid state."),
    ("Write down the Sum and Carry output expression for the full adder.", 
     "Sum = A XOR B XOR Cin\nCarry = AB + BCin + ACin"),
    ("State one disadvantage of S-R Flip Flop and how to overcome it.", 
     "Disadvantage: Invalid state at S=1, R=1. Overcome by using a JK Flip-flop."),
    ("State one disadvantage of J-K Flip Flops.", 
     "Disadvantage: Susceptible to Race Around Condition (overcome by Master-Slave configuration)."),
    ("What is a synchronous counter?", 
     "A counter where all flip-flops are triggered simultaneously by the same clock signal, reducing propagation delay errors.")
]

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.chapter_body(qa_data)
pdf.output("Sequential_Circuits_QA.pdf")

print("PDF created successfully: Sequential_Circuits_QA.pdf")