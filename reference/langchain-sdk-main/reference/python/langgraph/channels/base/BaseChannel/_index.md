---
title: "reference/python/langgraph/channels/base/BaseChannel"
description: "Index of 12 pages and 0 subdirectories under reference/python/langgraph/channels/base/BaseChannel."
category: "index"
tags: [index, reference, python, langgraph, channels, base, basechannel]
---

# reference/python/langgraph/channels/base/BaseChannel

12 pages here.

## Files

- [UpdateType](UpdateType.md) - The type of the update received by the channel.
- [ValueType](ValueType.md) - The type of the value stored in the channel.
- [checkpoint](checkpoint.md) - Return a serializable representation of the channel's current state.
- [consume](consume.md) - Notify the channel that a subscribed task ran.
- [copy](copy.md) - Return a copy of the channel.
- [finish](finish.md) - Notify the channel that the Pregel run is finishing.
- [from_checkpoint](from_checkpoint.md) - Return a new identical channel, optionally initialized from a checkpoint.
- [get](get.md) - Return the current value of the channel.
- [is_available](is_available.md) - Return True if the channel is available (not empty), False otherwise.
- [key](key.md) - View source on GitHub
- [typ](typ.md) - View source on GitHub
- [update](update.md) - Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step.
