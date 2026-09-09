# Decision Rules

## 1. Introduction

Decision rules define how the system uses the information stored in the knowledge repository to make business decisions.

The rules are based on inventory availability, order quantity, reorder levels, and payment status.

## 2. Order Acceptance Rule

If the available stock is greater than or equal to the quantity requested by the customer, the order can be accepted.

**Rule:**

```text
IF stock >= order_quantity
THEN order = accepted
```

### Example

Available stock = 15

Order quantity = 5

Since 15 >= 5, the order can be accepted.

## 3. Insufficient Stock Rule

If the available stock is less than the requested order quantity, the order should be placed on hold.

**Rule:**

```text
IF stock < order_quantity
THEN order = on_hold
```

### Example

Available stock = 3

Order quantity = 10

Since 3 < 10, the order cannot be fulfilled immediately.

## 4. Reorder Rule

If the available stock reaches or falls below the reorder level, the system should recommend purchasing additional stock.

**Rule:**

```text
IF stock <= reorder_level
THEN generate_restocking_recommendation
```

### Example

Available stock = 8

Reorder level = 10

Since 8 <= 10, the system recommends restocking.

## 5. Payment Success Rule

An order can be confirmed when the payment has been successfully completed.

**Rule:**

```text
IF payment_status == successful
THEN order = confirmed
```

## 6. Payment Failure Rule

If the payment fails, the order should remain pending and should not be confirmed.

**Rule:**

```text
IF payment_status == failed
THEN order = pending
```

## 7. Combined Order Decision

The system can combine multiple rules when processing an order.

For example:

```text
IF stock >= order_quantity
AND payment_status == successful
THEN order = confirmed
```

If sufficient stock exists but payment has failed:

```text
IF stock >= order_quantity
AND payment_status == failed
THEN order = pending
```

## 8. Rule Priority

The system should first check whether the requested quantity is available.

After stock availability is determined, the payment status can be checked.

The general decision process is:

```text
Check Product
       ↓
Check Stock
       ↓
Is Stock Sufficient?
   ↓              ↓
 Yes              No
   ↓              ↓
Check Payment   Hold Order
   ↓
Payment Successful?
   ↓              ↓
 Yes              No
   ↓              ↓
Confirm Order   Keep Pending
```

## 9. Conclusion

These decision rules convert stored business knowledge into actionable decisions. They allow the system to automatically determine order status and identify when inventory needs to be replenished.
