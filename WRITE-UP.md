# Design Write-up: Daily Reflection Decision Tree

## Objective

The objective of this project is to design a deterministic system that transforms unstructured daily reflections into structured behavioral insights. The system aims to remove ambiguity by using predefined inputs and rule-based decision logic, ensuring consistent and interpretable outcomes.

---

## Problem Statement

Daily reflections are often subjective and inconsistent. Traditional journaling lacks structure, and AI-based systems may introduce variability or hallucination. The challenge is to create a system that:

* Standardizes reflection
* Provides meaningful insights
* Maintains consistency across users
* Avoids ambiguity and randomness

---

## Approach

The solution is implemented as a deterministic decision tree structured across three behavioral axes. Each axis represents a specific dimension of human behavior and is evaluated using a sequence of predefined questions followed by rule-based classification.

The system ensures that every user response leads to a clear outcome without relying on probabilistic interpretation.

---

## System Design

The decision tree follows a sequential structure:

START
→ Axis 1
→ Axis 2
→ Axis 3
→ Summary
→ End

Each axis consists of:

* Multiple question nodes
* A decision node
* A reflection node

Bridges are used to transition between axes while maintaining flow continuity.

---

## Axis Design

### Axis 1: Locus of Control

This axis evaluates whether the user demonstrates internal or external control.

* Internal control indicates ownership of actions and outcomes
* External control indicates reliance on external circumstances

The questions are designed to capture behavioral responses to challenges and decision-making patterns.

---

### Axis 2: Contribution vs Entitlement

This axis measures whether the user is focused on contributing value or expecting outcomes.

* Contribution reflects proactive engagement and value creation
* Entitlement reflects expectation of recognition or reward

The questions assess motivation and intent behind actions.

---

### Axis 3: Self vs Others Focus

This axis determines whether the user prioritizes personal goals or considers others.

* Self-focus indicates individual-centric thinking
* Others-focus reflects awareness of team and stakeholders

The questions evaluate perspective and decision influence.

---

## Decision Logic

Decision nodes map user responses to specific behavioral categories using predefined rules.

Example structure:

* Each rule follows the format: answer → target node
* Multiple conditions are evaluated sequentially
* The first matching condition determines the path

This ensures deterministic behavior with no ambiguity.

---

## Data Representation

The decision tree is implemented using a TSV (Tab-Separated Values) format.

Each node is represented as a row with the following fields:

* id: Unique identifier
* parentId: Reference to the previous node
* type: Node type
* text: Content displayed
* options: Available responses
* target: Navigation or decision mapping
* signal: Behavioral classification

This format allows easy scalability and structured representation.

---

## Deterministic Nature

The system is designed to be fully deterministic:

* Inputs are restricted to predefined options
* No randomness or probabilistic logic is used
* Same input sequence always produces the same output

This ensures reliability, repeatability, and interpretability.

---

## Guardrails

To prevent ambiguity and ensure correctness:

* Free-text input is not allowed
* All responses are constrained to predefined options
* Decision rules are explicitly defined
* All branches lead to a valid end state
* Invalid transitions are avoided

These guardrails ensure the system remains controlled and predictable.

---

## System Completeness

The decision tree is designed such that all possible paths lead to a summary and end node. This guarantees that no execution path results in a dead end or undefined behavior.

This was ensured by explicitly connecting all reflection nodes to subsequent bridge or summary nodes.

---

## Part B: Agent Implementation

A simple command-line agent is implemented to operationalize the decision tree.

The agent performs the following steps:

* Loads the TSV file into memory
* Starts execution from the START node
* Displays questions and collects user input
* Navigates through nodes based on responses
* Applies rule-based decisions
* Outputs reflections and final summary

This demonstrates how the decision tree can be transformed into an interactive system.

---

## Limitations

While the system provides structured insights, it has certain limitations:

* It does not capture complex emotional nuances
* It is limited to predefined scenarios
* It does not adapt dynamically to user behavior
* It depends on honest user input

---

## Future Improvements

Potential enhancements include:

* Expanding question sets for deeper analysis
* Introducing multi-day tracking of behavioral patterns
* Adding visualization dashboards
* Integrating controlled AI input classification

---

## Conclusion

This project demonstrates how structured, rule-based systems can convert subjective human reflection into consistent and actionable insights. By prioritizing deterministic design over probabilistic interpretation, the system ensures clarity, reliability, and scalability.

The approach highlights the importance of structured thinking in solving problems involving human behavior and decision-making.
