---
marp: true
theme: default
size: 16:9
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&family=DM+Mono:wght@400;500&display=swap');

  section {
    font-family: 'DM Sans', sans-serif;
    background: #0a0a0a;
    color: #f5f5f4;
    padding: 64px 76px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  /* ══ eyebrow tag ══ */
  .eyebrow {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 24px;
  }
  .eyebrow-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #ff2f2f;
    flex-shrink: 0;
  }
  .eyebrow-text {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: #737373;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  /* ══ headings ══ */
  h1 {
    font-size: 42px;
    font-weight: 600;
    color: #fafafa;
    line-height: 1.15;
    letter-spacing: -0.03em;
    margin: 0 0 10px 0;
  }

  h1 em {
    font-style: normal;
    color: #ffffff;
    opacity: 0.9;
  }

  .kicker {
    font-size: 16px;
    font-weight: 400;
    color: #a3a3a3;
    margin: 0 0 22px 0;
    max-width: 640px;
  }

  .rule {
    width: 32px;
    height: 2px;
    background: #2a2a2a;
    border-radius: 999px;
    margin-bottom: 26px;
  }

  /* ══ body text ══ */
  p, li {
    font-size: 20px;
    line-height: 1.6;
    color: #d4d4d4;
  }

  strong {
    color: #fafafa;
    font-weight: 600;
  }

  ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding-left: 0;
  }

  li::before {
    content: '';
    width: 16px;
    height: 16px;
    min-width: 16px;
    border-radius: 50%;
    background: #18181b;
    border: 1px solid #333333;
    margin-top: 4px;
    position: relative;
  }

  li::after {
    content: '';
    position: relative;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #ffb6b600;
    left: -22px;
    margin-top: 9px;
  }

  /* ══ code ══ */
  code {
    font-family: 'DM Mono', monospace;
    background: rgba(255,255,255,0.07);
    color: #fafafa;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 0.82em;
  }

  pre {
    background: #18181b;
    border: 1px solid #262626;
    border-radius: 10px;
    padding: 22px 26px;
    font-size: 17px;
    line-height: 1.55;
    box-shadow: 0 2px 10px rgba(0,0,0,0.35);
  }

  pre code {
    background: none;
    color: #e5e5e5;
    padding: 0;
  }

  /* ══ footer pagination ══ */
  section::after {
    font-family: 'DM Mono', monospace;
    font-size: 9px;
    color: #525252;
    letter-spacing: 0.08em;
    content: 'pandapower series · ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    position: absolute;
    bottom: 26px;
    right: 40px;
  }

  /* ══ cover / closing ══ */
  section.cover, section.closing {
    background: #050505;
    align-items: flex-start;
  }

  section.cover h1, section.closing h1 {
    font-size: 58px;
  }

  section.cover .kicker, section.closing .kicker {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    color: #a3a3a3;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  section.closing {
    align-items: center;
    text-align: center;
  }

  section.closing .eyebrow {
    justify-content: center;
  }
---

<!-- _class: cover -->

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">pandapower · youtube series</span>
</div>

<div class="kicker">learn-in-public · code along</div>

# Build networks.<br>Run load flows.<br>Read the <em>results.</em>

<div class="rule"></div>

<p style="max-width:520px;">Seven short episodes — from a two-bus network to transformers and outage simulation. Every line explained as it's typed.</p>

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 01</span>
</div>

# The 2-Bus Network
<div class="kicker">Building the simplest pandapower network from scratch</div>
<div class="rule"></div>

- `create_empty_network()` → net object with empty DataFrames
- `create_bus()` → adds a row to `net.bus`
- `create_ext_grid()` → sets the slack bus voltage
- `create_line()` → connects buses using a `std_type`
- `create_load()` → adds demand to a bus
- `runpp()` → solves the AC load flow

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 01</span>
</div>

# Reading the Results

- `net.res_bus.vm_pu` — solved voltage per bus (per-unit)
- `net.res_line.loading_percent` — how loaded each line is
- `net.res_line.pl_mw` — active power loss per line

<div class="rule"></div>

**Try it:** raise `p_mw`, then raise `length_km` — both drop voltage differently

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 02</span>
</div>

# Add and Remove a Load
<div class="kicker">How pandapower stores network state between runs</div>
<div class="rule"></div>

- `create_load()` returns an index — save it to modify later
- `net.load.drop(index, inplace=True)` removes a row
- Re-running `runpp()` always reflects current DataFrame state
- No hidden state — the result depends only on what's in `net` right now

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 02</span>
</div>

# The `in_service` Alternative

```python
net.load.at[load_b, 'in_service'] = False
```

- Same effect as dropping the row
- Row stays in the table — can be switched back on later
- pandapower skips any element where `in_service` is `False`

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 03</span>
</div>

# Change Line Impedance
<div class="kicker">Modifying a line parameter between runs</div>
<div class="rule"></div>

- Store the line's index at creation: `line_idx`
- Edit a single cell: `net.line.at[line_idx, 'length_km'] = 2.0`
- No need to rebuild the network — just edit and re-run

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 03</span>
</div>

# What Changes

- Longer line → more impedance → lower voltage, higher losses

<div class="rule"></div>

**Your turn:** swap conductor size with `pp.change_std_type()` instead of changing length

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 04</span>
</div>

# Results Summary Function
<div class="kicker">Writing a reusable function to read results</div>
<div class="rule"></div>

```python
total_load_mw    = net.res_load.p_mw.sum()
total_loss_mw    = net.res_line.pl_mw.sum()
min_voltage      = net.res_bus.vm_pu.min()
min_voltage_bus  = net.res_bus.vm_pu.idxmin()
max_loading      = net.res_line.loading_percent.max()
max_loading_line = net.res_line.loading_percent.idxmax()
```

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 04</span>
</div>

# Violation Checks

```python
if min_voltage < 0.95:
    print(f"VOLTAGE VIOLATION at Bus {min_voltage_bus}!")
if max_loading > 100:
    print(f"OVERLOAD on Line {max_loading_line}!")
```

<div class="rule"></div>

- `idxmin()` / `idxmax()` find the *worst* element automatically
- Works on any network — nothing hardcoded

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 05</span>
</div>

# Loop Over Load Scenarios
<div class="kicker">Running multiple load flows in a loop</div>
<div class="rule"></div>

```python
for load_mw in load_levels_mw:
    net.load.at[load_idx, 'p_mw'] = load_mw
    pp.runpp(net)
    voltages.append(net.res_bus.vm_pu[b2])
    losses.append(net.res_line.pl_mw.sum())
```

- Same network, six solves, two result lists

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 05</span>
</div>

# Visualizing Results

- `matplotlib` line plot: load (MW) vs. voltage (pu)
- `axhline(y=0.95)` marks the violation threshold

<div class="rule"></div>

**Your turn:** add a third list tracking max line loading per scenario

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 06</span>
</div>

# Two Parallel Lines
<div class="kicker">Using in_service to simulate a line outage</div>
<div class="rule"></div>

- Two `create_line()` calls between the same buses = two parallel paths
- With both in service, current splits between them
- Set one to `in_service = False` → all current shifts to the other

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 06</span>
</div>

# Current Redistribution

- `net.res_line.i_ka` shows real current, `loading_percent` shows relative loading
- Taking one line out roughly **doubles** loading on the other

<div class="rule"></div>

**Your turn:** make lines different lengths — the split becomes proportional to admittance, not 50/50

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 07</span>
</div>

# Transformer Basic Model
<div class="kicker">Connecting voltage levels and reading per-unit results</div>
<div class="rule"></div>

- Two buses at different `vn_kv` (20 kV and 0.4 kV)
- `create_transformer()` links them via a `std_type`
- Slack sits on the HV side; load sits on the LV side

---

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">episode 07</span>
</div>

# Converting Per-Unit to Real Voltage

```python
net.res_bus.vm_pu[hv_bus] * 20          # kV
net.res_bus.vm_pu[lv_bus] * 0.4 * 1000  # V
```

<div class="rule"></div>

- `net.res_trafo.loading_percent` — how loaded the transformer is
- `net.res_trafo.pl_mw` — transformer active power loss

---

<!-- _class: closing -->

<div class="eyebrow">
  <div class="eyebrow-dot"></div>
  <span class="eyebrow-text">pandapower · youtube series</span>
</div>

# Thanks for watching

<div class="rule"></div>

<p>Code along, break things, re-run.</p>