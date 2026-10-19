D1 需求忠实度，权重0.35

5：完全捕获需求，且没有不受支持的强化。
4：捕获了主要需求，仅存在轻微遗漏或措辞问题。
3：部分捕获需求，但遗漏或弱化了一些相关行为。
2：主要需求意图缺失或被明显扭曲。
1：与核心需求相矛盾，或忽略核心需求。

D2 架构扎根性，权重0.25

5：所有标识符、端口、owner和作用域都充分扎根于AADL上下文。
4：整体扎根较好，仅存在轻微命名或放置问题。
3：使用了一些正确的架构元素，但作用域或扎根性存在疑问。
2：存在严重架构扎根错误。
1：依赖编造的或明显无效的架构引用。

D3 形式化充分性，权重0.20

5：条件、义务和形式关系被完整且恰当地表达。
4：形式化总体充分，仅存在轻微不完整。
3：形式化具有部分作用，但不完整。
2：形式化遗漏了主要逻辑关系，或使用了不合适的构造。
1：形式内容无法用于该需求。

D4 不受支持内容控制，权重0.10

5：没有不受支持的谓词、阈值、变量或额外行为。
4：存在轻微不受支持的措辞或无害的额外结构。
3：存在一些可疑的不受支持内容，但不是核心问题。
2：存在严重不受支持的关系或编造行为。
1：输出严重依赖编造内容或需求外部内容。

D5 可审查性，权重0.10

5：易于审查；标签、结构和编辑清晰。
4：总体可审查，仅存在轻微清晰度问题。
3：需要一定努力才能审查。
2：难以检查或追踪。
1：实际不可审查。

---

D1 Requirement Fidelity, weight 0.35
5: Fully captures the requirement without unsupported strengthening.
4: Captures the main requirement with only minor omissions or wording issues.
3: Partially captures the requirement but misses or weakens some relevant behavior.
2: Major requirement intent is missing or substantially distorted.
1: Contradicts or ignores the core requirement.

D2 Architectural Grounding, weight 0.25
5: All identifiers, ports, owners, and scopes are well grounded in the AADL context.
4: Mostly grounded, with minor naming or placement concerns.
3: Uses some correct architectural elements but has questionable scope or grounding.
2: Contains major grounding errors.
1: Relies on fabricated or clearly invalid architecture references.

D3 Formalization Adequacy, weight 0.20
5: Conditions, obligations, and formal relations are expressed completely and appropriately.
4: Formalization is mostly adequate with minor incompleteness.
3: Formalization is partially useful but incomplete.
2: Formalization omits major logical relations or uses unsuitable constructs.
1: Formal content is unusable for the requirement.

D4 Unsupported-Content Control, weight 0.10
5: No unsupported predicates, thresholds, variables, or extra behaviors.
4: Minor unsupported wording or harmless extra structure.
3: Some questionable unsupported content, but not central.
2: Major unsupported relation or invented behavior.
1: Output heavily depends on fabricated or requirement-external content.

D5 Reviewability, weight 0.10
5: Easy to review; labels, structure, and edits are clear.
4: Mostly reviewable with minor clarity issues.
3: Reviewable with effort.
2: Difficult to inspect or trace.
1: Not practically reviewable.

总分：

```
S_{\mathrm{expert}} =
0.35D_1 + 0.25D_2 + 0.20D_3 + 0.10D_4 + 0.10D_5.
```