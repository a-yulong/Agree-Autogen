# GF_Monitor Example

This is a minimal illustrative example for AGREE-AutoGen.

Files:

- `requirement.txt`: natural-language requirement.
- `input.aadl`: base AADL model.
- `expected_output.aadl`: illustrative fused AADL+AGREE artifact.

Semantics:

- `latitude` and `longitude` are input ports.
- `gfReq` and `alarm_out` are output ports.
- When `latitude = 10.0` and `longitude = 15.0`, `gfReq` is activated.
- When the fence violation condition holds, `alarm_out` is triggered.

The expected output is intentionally compact. It should be checked with a local OSATE/AGREE installation before being used as a validated benchmark artifact.

