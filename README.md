# Project Strikethrough

> How is your day? How is your week? How is your year? Did curiosity really kill the cat? Or was it ennui of the mundane?

**Strikethrough** is the command-line interface and distribution layer for **Skywatch**, an autonomous, locally operable, recursively self-improving software system.

Strikethrough provides a convenient interface for installing, configuring, launching, monitoring, and managing Skywatch without requiring users to interact directly with its underlying Python module.

Skywatch; however, is considerably more than a background daemon.

It is designed to identify limitations, analyze its available resources, determine possible solutions, and attempt to overcome those limitations by modifying its own software, runtime, dependencies, and capabilities.

This repository documents both projects, their intended applications, and the risks associated with their operation.

---

# Table of Contents

- 1\. Introduction to Skywatch
- 2\. What Can Skywatch Do?
- 3\. Recursive Self-Improvement
- 4\. Inference and Context Engineering
- 5\. Skywatch Runtime
- 6\. Project Strikethrough
- 7\. Installation
- 8\. CLI Reference
- 9\. Command Behavior
- 10\. Configuration
- 11\. Logs and Inspection
- 12\. Security Considerations and Dangers
- 13\. Official Disclosure
- 14\. Philosophy

---

# 1\. Introduction to Skywatch

Skywatch is an autonomous software system designed around persistent operation, agentic workflows, and recursive self-improvement.

Unlike conventional AI assistants; which generally operate within a predetermined set of capabilities, Skywatch is designed to attempt to modify and extend the environment in which it operates.

Its intended scope of improvement includes:

- **Runtime:** Modifying and improving its own execution environment.
- **Dependencies:** Managing and improving locally installed software dependencies.
- **Model weights:** Attempting to modify accessible local model weights where needed.
- **Software:** Analyzing and modifying its own implementation.
- **Capabilities:** Developing functionality that was not originally available in its base implementation.

The defining characteristic of Skywatch is that it does not necessarily have to accept an encountered limitation as permanent.

It can attempt to understand the limitation, evaluate available resources, formulate an appropriate action, verify the proposed solution, and execute an attempt to overcome it.

This makes Skywatch both a practical autonomous software tool and an experimental platform for recursive software improvement.

# 2\. What Can Skywatch Do?

Skywatch is not exclusively an experiment in recursive self-improvement.

It has several practical applications that make it useful independently of its more ambitious architectural goals.

## 2.1 Machine and System Maintenance

Skywatch can be applied to the maintenance of local machines and software environments.

Potential applications include:

- Software environment maintenance.
- Dependency management.
- Identifying and addressing software limitations.
- Automating maintenance workflows.
- Analyzing system behavior.
- Responding to detected operational issues.

## 2.2 Workflow Management

Skywatch is designed to handle complex workflows involving multiple operations, decisions, and dependencies.

Potential applications include:

- Multi-stage workflow automation.
- Long-running tasks.
- Project-level task management.
- Automated development workflows.
- Persistent background operations.
- Complex task decomposition.

## 2.3 Advanced Software Development

Skywatch can be used as an autonomous software development system.

Its intended capabilities extend beyond modifying ordinary application code.

Potential applications include:

- Building advanced software.
- Maintaining existing applications.
- Developing new functionality.
- Managing dependencies.
- Iterative software improvement.
- Modifying its own implementation.

## 2.4 Persistent Monitoring

Skywatch's daemon architecture allows it to remain operational in the background.

This makes it suitable for applications involving persistent observation, recurring tasks, and ongoing workflows.

Rather than requiring a user to manually initiate every interaction, Skywatch can maintain an ongoing operational presence.

## 2.5 Entirely Local Agentic Workflows

Skywatch can operate using locally available infrastructure and inference resources.

This enables deployments that prioritize:

- Local inference.
- Reduced dependence on external inference APIs.
- Greater control over accessible data.
- Locally installed dependencies.
- Persistent autonomous operation.
- Reduced recurring inference costs when local infrastructure is economical.

## 2.6 Large-Scale Multi-Step Workflows

Skywatch is intended to handle tasks that require more than a single interaction or are constrained by a limited context window.

Its context management architecture is designed to maintain relevant information across complex and extended tasks.

Examples include:

- Large software projects.
- Extended development sessions.
- Complex dependency relationships.
- Long-running autonomous workflows.
- Persistent project understanding.

# 3\. Recursive Self-Improvement

Recursive self-improvement is the defining architectural ambition of Skywatch.

The system is designed around a recurring limitation-resolution process.

## 3.1 The Improvement Cycle

The conceptual process is:

**Encounter → Analyze → Evaluate → Decide → Verify → Execute**

Each stage has a distinct purpose.

1. **Encounter:** Skywatch encounters a limitation in its current capabilities or environment.
2. **Analyze:** Skywatch investigates the limitation and attempts to understand its underlying cause.
3. **Evaluate:** Skywatch evaluates available resources, tools, dependencies, and possible modifications.
4. **Decide:** Skywatch determines an action intended to overcome the limitation.
5. **Verify:** Skywatch evaluates the proposed action and attempts to establish whether it addresses the identified problem.
6. **Execute:** Skywatch executes the selected action in an attempt to invalidate the limitation.

The process can repeat as new limitations emerge.

The objective is not simply to complete an individual task, instead to improve the system's ability to complete tasks that were previously beyond its capabilities.

## 3.2 Capability Expansion

An important distinction is that Skywatch is not limited to improving existing functionality.

It is also designed to attempt to develop entirely new capabilities.

For example, a limitation might originate from missing functionality in the base implementation.

Rather than necessarily treating that functionality as permanently unavailable, Skywatch may attempt to develop an implementation that provides it.

The success of such attempts depends on the underlying model, available resources, permissions, environment, and implementation constraints.

## 3.3 Theoretical Implications

Recursive self-improvement introduces risks that deserve serious consideration.

A sufficiently capable system with access to substantial computational resources and its own implementation could theoretically produce increasingly capable iterations.

At an extreme theoretical threshold, this raises questions concerning Artificial Superintelligence (ASI).

One particularly concerning hypothetical scenario resembles a Paperclip Maximizer event.

In this analogy; the objective being maximized is not the production of paperclips; instead, recursive self-improvement itself.

An inadequately constrained system pursuing such an objective could theoretically prioritize its continued improvement over other considerations.

This is a theoretical discussion, not a claim that Skywatch has achieved ASI or that such an outcome is inevitable.

**The possibility of increasingly capable recursive self-improvement should not be treated as an invitation to experimentally pursue uncontrolled outcomes.**

# 4\. Inference and Context Engineering

Skywatch incorporates techniques intended to improve inference efficiency and maintain understanding across complex workloads.

These techniques are important to making local and resource-constrained deployments practical.

## 4.1 Model Quantization

Skywatch can work with model quantization techniques to reduce the memory requirements of local inference.

Quantization can make otherwise impractical models more accessible to hardware with limited memory capacity.

## 4.2 KV-Cache Quantization

KV-cache quantization is another component of Skywatch's inference optimization capabilities.

Reducing KV-cache memory consumption can help manage the memory requirements associated with extended context windows.

## 4.3 LoRA and QLoRA

Skywatch supports working with LoRA and QLoRA techniques.

These approaches enable parameter-efficient model adaptation without necessarily requiring the full computational and memory costs of conventional full-model fine-tuning.

## 4.4 Retrieval-Augmented Generation

Skywatch uses Retrieval-Augmented Generation (RAG) as part of its context management approach.

RAG helps maintain access to relevant information when working with large and complex tasks.

Rather than relying exclusively on information currently present in the active context, relevant information can be retrieved as needed.

## 4.5 Advanced Context Budgeting

Skywatch incorporates an advanced context budgeting formula supported by RAG.

Its purpose is to manage the available context while maintaining relevant information about ongoing tasks.

This is particularly important when dealing with:

- Large codebases.
- Extended software development sessions.
- Complex projects.
- Long-running workflows.
- Large quantities of accumulated information.

The intention is to preserve useful task understanding without treating the context window as an unlimited resource.

# 5\. Skywatch Runtime

Skywatch is the underlying runtime managed by Strikethrough.

It is implemented as a Python module and can be invoked directly.

bash

```bash
python3 -m skywatch -h
```

The runtime provides several operational interfaces.

| Argument | Purpose |
| --- | --- |
| `-l`, `--launch` | Launch Skywatch. |
| `-s`, `--send` | Submit an administrative message. |
| `-c`, `--configure` | Configure Skywatch. |
| `-d`, `--delete-session` | Delete a chat session. |
| `-q`, `--quit` | Request Skywatch to quit. |
| `-t`, `--terminate` | Directly terminate Skywatch at the process level. |
| `-v`, `--view` | Read a Skywatch file or execution log. |

Skywatch daemonizes itself when launched.

Consequently, launching the runtime does not require the invoking terminal to remain open.

Administrative messages can also be submitted before the daemon is running. Such messages remain pending until Skywatch launches and can intercept and process them.

Strikethrough provides a more convenient interface for these operations.

# 6\. Project Strikethrough's Interface

Strikethrough is the command-line interface and installation layer for Skywatch.

It abstracts the underlying Python runtime into a more approachable command structure.

The intended command alias is:

bash

```bash
scli
```

The command `strikethrough` is also usable for less ambiguity.

Strikethrough is primarily a wrapper. It is not intended to replace Skywatch's underlying runtime or independently reproduce its functionality.

Its responsibilities include:

- Installing the Skywatch runtime.
- Extracting and decrypting the runtime source.
- Launching the Skywatch daemon.
- Configuring Skywatch.
- Sending administrative messages.
- Managing daemon shutdown.
- Managing chat sessions.
- Inspecting execution logs.
- Inspecting configuration.

# 7\. Installation

Install Strikethrough using the distribution method provided by the project.

Once installed, the CLI can be invoked using:

bash

```bash
scli
```

Display available commands:

bash

```bash
scli --help
```

## 7.1 Installing Skywatch

bash

```bash
scli install
```

Installs the Skywatch runtime.

A custom installation path can optionally be supplied:

bash

```bash
scli install /path/to/skywatch
```

## 7.2 Decrypting Skywatch Without Running Build Code

bash

```bash
scli decrypt_only /path/to/destination
```

This command installs Skywatch by decrypting its raw source without executing build code.

It is intended for users who want to obtain the decrypted runtime source without initiating the build or installation execution process.

**Important:** Decrypting source without executing build code is not equivalent to verifying that the source is safe. The resulting source should still be inspected before execution.

# 8\. CLI Reference

The following commands constitute the Strikethrough interface.

| Command | Description |
| --- | --- |
| `scli install [custom_path]` | Install or reinstall the Skywatch runtime. |
| `scli decrypt_only <path>` | Decrypt and extract Skywatch source without running build code. |
| `scli launch` | Launch the Skywatch daemon. Installs Skywatch first if missing. |
| `scli configure <key=value>` | Configure Skywatch's `model.json` file. |
| `scli send <message>` | Send an administrative message to Skywatch. |
| `scli quit` | Send a quit instruction to Skywatch. |
| `scli terminate` | Forcibly terminate the Skywatch process. |
| `scli erase_session <session_name>` | Delete a chat memory session. |
| `scli logs <N\|current>` | View an execution log. |
| `scli print_config` | Print Skywatch's configuration. |
| `scli is_alive` | Check if Skywatch is alive. |

# 9\. Commands

## 9.1 install

bash

```bash
scli install
scli install /custom/path
```

Installs the Skywatch runtime.

The optional argument specifies a custom installation location.

## 9.2 decrypt\_only

bash

```bash
scli decrypt_only /path/to/destination
```

Decrypts and extracts the raw Skywatch source without executing build code.

This operation is separate from the regular installation process.

It is intended for source inspection and manual handling.

## 9.3 launch

bash

```bash
scli launch
```

Launches the Skywatch daemon.

If Skywatch has not been installed, Strikethrough installs it first.

Skywatch daemonizes itself, allowing it to continue operating in the background.

## 9.4 configure

bash

```bash
scli configure key=value
```

Configures Skywatch's `model.json` file.

The argument is supplied using a `key=value` format.

Example:

bash

```bash
scli configure chat_engine=Qwen/Qwen3.8-27B
```

The accepted configuration keys and values depend on Skywatch's implementation.

## 9.5 send

bash

```bash
scli send "Your objective goes here."
```

Submits an administrative message to Skywatch.

The message is handled by the Skywatch daemon when available.

If Skywatch is not running, the message remains pending until the daemon launches.

This behavior is inherited from the underlying Skywatch runtime.

**Sending a message does not require Skywatch to already be running.**

## 9.6 quit

bash

```bash
scli quit
```

Sends a quit instruction to the Skywatch daemon.

This is the intended way to request a normal shutdown.

## 9.7 terminate

bash

```bash
scli terminate
```

Directly terminates the Skywatch process at the process level.

Unlike `quit`, this does not rely on the normal daemon shutdown instruction.

Use this command cautiously, as forcibly terminating a process can interrupt ongoing operations.

## 9.8 erase\_session

bash

```bash
scli erase_session session_name
```

Deletes the specified Skywatch chat memory session.

This is intended for managing individual persistent conversation sessions.

## 9.9 logs

bash

```bash
scli logs 1
scli logs 5
scli logs current
```

Displays a Skywatch execution log.

The argument accepts either:

- A numeric log identifier.
- The keyword `current`, which requests the current execution log.

## 9.10 print\_config

bash

```bash
scli print_config
```

Prints Skywatch's current configuration.

This provides a convenient way to inspect the configuration stored in `model.json`.

# 10\. Configuration

Skywatch uses `model.json` as its configuration file.

Strikethrough exposes configuration through:

bash

```bash
scli configure key=value
```

Configuration options determine aspects of Skywatch's operation, including the settings consumed by its underlying `model.py` implementation.

To inspect the current configuration:

bash

```bash
scli print_config
```

Users should consult the corresponding Skywatch implementation when determining the behavior of individual configuration options.

# 11\. Logs and Inspection

Skywatch provides a mechanism for inspecting execution logs and configuration files.

Strikethrough exposes this functionality through two commands.

**View an execution log:**

bash

```bash
scli logs current
```

**View a numbered execution log:**

bash

```bash
scli logs 3
```

**Print the current configuration:**

bash

```bash
scli print_config
```

**Check if Skywatch is alive:**

bash

```bash
scli is_alive
```

Execution logs are useful for understanding runtime behavior, investigating errors, and reviewing previous execution activity.

# 12\. Security Considerations and Dangers

Skywatch is an autonomous system designed to modify software and potentially expand its own capabilities.

This introduces risks that are not necessarily present in conventional software applications.

Users should understand the implications of granting an autonomous system access to their local environment.

## 12.1 Autonomous Software Modification

Skywatch may attempt to modify its own implementation and accessible dependencies.

Incorrect modifications can introduce software defects, instability, compatibility issues, or unexpected behavior.

Self-modification should not be assumed to be inherently safe merely because the system attempts to verify its actions.

## 12.2 Local Environment Access

Depending on deployment and permissions, Skywatch may have access to local files, software, dependencies, and other resources.

The consequences of unintended modifications depend on the permissions granted to the process.

Users should avoid granting unnecessary privileges.

## 12.3 Model and Dependency Integrity

Locally installed models, model weights, and software dependencies may be modified when accessible to the system.

Changes can affect model behavior, reproducibility, and software integrity.

Users should maintain backups of important resources and verify changes before relying on modified components.

## 12.4 Persistent Operation

Skywatch is designed to run as a background daemon.

Persistent operation means that its actions may continue beyond the lifetime of the terminal session that launched it.

Users should understand how to inspect, stop, and manage the running process.

## 12.5 Recursive Self-Improvement

The most significant theoretical risk comes from the possibility of recursive capability expansion.

A system capable of modifying its own implementation may introduce changes that affect its subsequent behavior and modification capabilities.

The consequences of increasingly capable autonomous systems are difficult to predict.

Unrestricted recursive self-improvement should not be treated as a harmless experiment.

## 12.6 Deployment Recommendations

Users should consider the following precautions:

- Run Skywatch with only the permissions it requires.
- Maintain backups of important files and configurations.
- Inspect decrypted source before executing it.
- Understand the consequences of modifying local dependencies and model weights.
- Monitor persistent daemon activity.
- Avoid granting unrestricted access to sensitive environments.
- Maintain a reliable method of terminating the process.
- Do not assume that autonomous verification guarantees correctness.

**Users are responsible for the environments in which they deploy Skywatch and the permissions they grant it.**

# 13\. Official Disclosure

Skywatch maintains an official disclosure documenting additional considerations concerning the project.

It should be read before deploying or experimenting with the runtime.

**Official Skywatch Disclosure:**

https://knexyce-co.github.io/skywatch\_disclosure/

Our disclosure is an oversimplified, yet accurate example of what Skywatch is.

# 14\. Philosophy

Strikethrough exists to make Skywatch accessible without requiring users to manually manage its underlying runtime.

Skywatch itself represents a broader idea: software should not necessarily be limited to the capabilities present at the moment it is first executed.

A system that can identify its limitations, reason about potential improvements, and attempt to implement them introduces a different approach to autonomous software engineering.

This has practical applications in maintenance, development, monitoring, workflow automation, and local inference.

It also introduces significant theoretical and operational risks that deserve equal attention.

The intention is to explore both sides of that capability.

**Build software. Maintain systems. Overcome limitations.**

And perhaps, occasionally, question the limitations themselves.

---

_Project Strikethrough; the interface to Skywatch._
