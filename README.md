# Daily Reflection Decision Tree

## Overview

This project implements a deterministic decision tree system to structure daily reflections into meaningful and actionable insights. Instead of relying on unstructured journaling or probabilistic AI outputs, the system uses predefined questions and rule-based logic to analyze user behavior across multiple dimensions.

The goal is to transform subjective experiences into structured evaluation, ensuring clarity, consistency, and interpretability.

---
## What this project demonstrates

This project demonstrates how human reflection can be structured into a deterministic system using rule-based decision trees instead of relying on probabilistic AI models.

---
## Objective

The objective of this project is to:

* Convert daily user reflections into structured inputs
* Apply deterministic logic to evaluate behavioral patterns
* Generate consistent insights based on predefined rules
* Eliminate ambiguity and reduce reliance on subjective interpretation

---

## System Architecture

The system is designed as a sequential decision tree with three major analytical axes:

### Axis 1: Locus of Control

This axis evaluates whether the user demonstrates:

* Internal control (taking responsibility for actions)
* External control (attributing outcomes to external factors)

### Axis 2: Contribution vs Entitlement

This axis measures whether the user:

* Focuses on contributing value
* Focuses on receiving recognition or outcomes

### Axis 3: Self vs Others Focus

This axis determines whether the user:

* Prioritizes personal outcomes
* Considers team, colleagues, or broader stakeholders

---

## Flow of Execution

The system follows a fixed sequence:

START
→ Axis 1 (Questions → Decision → Reflection)
→ Bridge
→ Axis 2 (Questions → Decision → Reflection)
→ Bridge
→ Axis 3 (Questions → Decision → Reflection)
→ Summary
→ End

Each axis contains multiple questions, followed by a decision node that maps responses to behavioral categories.

---

## Flowchart

The visual representation of the decision tree is shown below:

![Decision Tree Flowchart] (Decision Tree Flowchart.png)

---

## Data Representation

The decision tree is implemented using a TSV (Tab-Separated Values) file.

Each row represents a node in the system with the following structure:

* id: Unique identifier for the node
* parentId: Reference to the previous node
* type: Node type (start, question, decision, reflection, bridge, summary, end)
* text: Content displayed to the user
* options: Available responses (for question nodes)
* target: Mapping for decision or navigation
* signal: Behavioral classification

---

## Deterministic Design

The system is fully deterministic:

* All inputs are predefined
* All transitions follow fixed rules
* No randomness is involved
* Same inputs always produce the same output

This ensures consistency, reproducibility, and interpretability.

---

## Guardrails

To ensure reliability and prevent ambiguity:

* Only predefined options are allowed
* No free-text input is processed
* Decision logic is rule-based
* All branches lead to a valid conclusion
* Invalid or incomplete states are avoided

---

## Part A: Decision Tree

The core of the project is the decision tree defined in `reflection-tree.tsv`.

It:

* Structures user reflection into multiple stages
* Applies rule-based classification
* Produces insights and a final summary
* Ensures all paths lead to completion

---

## Part B: Agent Implementation

A simple command-line agent is implemented using Python to execute the decision tree.

The agent:

* Loads the TSV file
* Traverses nodes sequentially
* Displays questions to the user
* Accepts input through numbered options
* Applies decision rules to navigate the tree
* Outputs reflections and final summary

### How to Run

1. Open terminal in the project folder

2. Run the following command:

   python agent.py

3. Follow the prompts and select options by entering numbers

---

## Project Structure

daily-reflection-tree/

* reflection-tree.tsv   → Decision tree definition
* agent.py              → CLI-based execution agent
* write-up.md           → Design explanation
* README.md             → Project documentation
* tree-diagram.png      → Flowchart visualization

---

## Strengths

* Clear and structured design
* Deterministic and interpretable logic
* No dependency on external AI models
* Consistent and reproducible outputs
* Easy to extend with additional nodes

---

## Limitations

* Does not capture nuanced emotional states
* Limited to predefined scenarios
* No dynamic adaptation
* Relies on user honesty

---

## Conclusion

This project demonstrates how structured decision systems can convert unstructured human reflection into consistent and actionable insights. By prioritizing deterministic logic over probabilistic interpretation, the system ensures clarity, reliability, and transparency in behavioral evaluation.

---

## Technologies Used

* Python
* TSV (Tab-Separated Values)
* VS Code
* draw.io (for flowchart)
* GitHub

---
## Design Focus

The system prioritizes interpretability and structured reasoning over automation, ensuring that each decision can be traced and understood.
