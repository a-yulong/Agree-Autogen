from agree_autogen.case_runner import _collect_declared_component_names


def test_collect_component_names_from_toy_aadl():
    aadl = """
package Toy
public
  system GF_Monitor
    features
      latitude: in data port Base_Types::Float;
  end GF_Monitor;

  system implementation GF_Monitor.impl
  end GF_Monitor.impl;
end Toy;
"""
    names = _collect_declared_component_names(aadl)
    assert "GF_Monitor" in names
    assert "GF_Monitor.impl" in names

