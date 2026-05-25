from odoo import models, fields, api
from odoo.exceptions import ValidationError


class KnowledgeCategory(models.Model):
    _name = 'knowledge.category'
    _description = 'Knowledge Category'

    name = fields.Char(required=True)

    available_parent_ids = fields.Many2many(
        'knowledge.category',
        compute='_compute_available_parents'
    )

    parent_id = fields.Many2one(
        'knowledge.category',
        string='Parent Category',
        domain="[('id', 'in', available_parent_ids)]"
    )

    child_ids = fields.One2many(
        'knowledge.category',
        'parent_id',
        string='Children'
    )


    def _dfs_children(self, node, visited=None):

        if visited is None:
            visited = set()

        if not node:
            return visited

        visited.add(node.id)

        for child in node.child_ids:
            self._dfs_children(child, visited)

        return visited

    @api.depends('parent_id')
    def _compute_available_parents(self):

        all_categories = self.search([])

        for record in self:
            forbidden_ids = record._dfs_children(record)

            allowed = all_categories.filtered(
                lambda c: c.id not in forbidden_ids
            )

            record.available_parent_ids = allowed