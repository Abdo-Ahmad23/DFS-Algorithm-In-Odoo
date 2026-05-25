# Odoo Knowledge Category

A custom Odoo module for hierarchical knowledge categories.

## Features
- Parent/Child categories
- Prevent circular hierarchy
- Dynamic parent filtering
- DFS recursion to detect descendants

## Example

Allowed:

Programming
└── Python

Not Allowed:

Programming
└── Python
    └── Programming
