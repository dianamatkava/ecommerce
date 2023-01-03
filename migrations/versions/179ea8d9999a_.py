"""empty message

Revision ID: 179ea8d9999a
Revises: 
Create Date: 2023-01-03 21:46:36.556759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '179ea8d9999a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.String(length=225), nullable=False),
    sa.Column('promo', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_card'))
    )
    op.create_table('company_logo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=125), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_company_logo'))
    )
    op.create_table('currency',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('abr', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_currency'))
    )
    op.create_table('customer_avatar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=125), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_customer_avatar'))
    )
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=225), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_category'))
    )
    op.create_table('product_component',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_component'))
    )
    op.create_table('product_custom_field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=225), nullable=False),
    sa.Column('short_name', sa.String(length=225), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_custom_field'))
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=125), nullable=False),
    sa.Column('password', sa.String(length=125), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.Column('img', sa.Integer(), nullable=True),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['img'], ['customer_avatar.id'], name=op.f('fk_customer_img_customer_avatar')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_customer')),
    sa.UniqueConstraint('email', name=op.f('uq_customer_email'))
    )
    op.create_table('promotion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=1255), nullable=True),
    sa.Column('discount_type', sa.Enum('fixed', 'persent', name='discounttype'), nullable=False),
    sa.Column('discount_value', sa.Integer(), nullable=True),
    sa.Column('coupon_type', sa.Enum('single', 'multiple', name='coupontype'), nullable=False),
    sa.Column('currency_id', sa.Integer(), nullable=True),
    sa.Column('start_day', sa.DateTime(), nullable=True),
    sa.Column('end_day', sa.DateTime(), nullable=True),
    sa.Column('instant_discount', sa.Boolean(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], name=op.f('fk_promotion_currency_id_currency')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_promotion'))
    )
    op.create_table('seller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=125), nullable=False),
    sa.Column('password', sa.String(length=125), nullable=False),
    sa.Column('role', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('company_name', sa.String(length=125), nullable=True),
    sa.Column('country', sa.String(length=125), nullable=True),
    sa.Column('img', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['img'], ['company_logo.id'], name=op.f('fk_seller_img_company_logo')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_seller')),
    sa.UniqueConstraint('email', name=op.f('uq_seller_email'))
    )
    op.create_table('coupon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=18), nullable=True),
    sa.Column('promotion_id', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotion.id'], name=op.f('fk_coupon_promotion_id_promotion')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_coupon'))
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=225), nullable=False),
    sa.Column('description', sa.String(length=1500), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('currency_id', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], name=op.f('fk_product_currency_id_currency')),
    sa.ForeignKeyConstraint(['owner_id'], ['seller.id'], name=op.f('fk_product_owner_id_seller')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
    )
    op.create_table('promotions',
    sa.Column('promotion_id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotion.id'], name=op.f('fk_promotions_promotion_id_promotion')),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], name=op.f('fk_promotions_seller_id_seller')),
    sa.PrimaryKeyConstraint('promotion_id', 'seller_id', name=op.f('pk_promotions'))
    )
    op.create_table('active_codes_for_custmr',
    sa.Column('coupon_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['coupon_id'], ['coupon.id'], name=op.f('fk_active_codes_for_custmr_coupon_id_coupon')),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name=op.f('fk_active_codes_for_custmr_customer_id_customer')),
    sa.PrimaryKeyConstraint('coupon_id', 'customer_id', name=op.f('pk_active_codes_for_custmr'))
    )
    op.create_table('active_codes_for_sel',
    sa.Column('coupon_id', sa.Integer(), nullable=False),
    sa.Column('seller_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['coupon_id'], ['coupon.id'], name=op.f('fk_active_codes_for_sel_coupon_id_coupon')),
    sa.ForeignKeyConstraint(['seller_id'], ['seller.id'], name=op.f('fk_active_codes_for_sel_seller_id_seller')),
    sa.PrimaryKeyConstraint('coupon_id', 'seller_id', name=op.f('pk_active_codes_for_sel'))
    )
    op.create_table('coupons',
    sa.Column('promotion_id', sa.Integer(), nullable=False),
    sa.Column('coupon_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['coupon_id'], ['coupon.id'], name=op.f('fk_coupons_coupon_id_coupon')),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotion.id'], name=op.f('fk_coupons_promotion_id_promotion')),
    sa.PrimaryKeyConstraint('promotion_id', 'coupon_id', name=op.f('pk_coupons'))
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product'], ['product.id'], name=op.f('fk_order_product_product')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order'))
    )
    op.create_table('product_categories',
    sa.Column('product_category_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_category_id'], ['product_category.id'], name=op.f('fk_product_categories_product_category_id_product_category')),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_product_categories_product_id_product')),
    sa.PrimaryKeyConstraint('product_category_id', 'product_id', name=op.f('pk_product_categories'))
    )
    op.create_table('product_component_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_component_id', sa.Integer(), nullable=False),
    sa.Column('product_custom_field_id', sa.Integer(), nullable=False),
    sa.Column('item_sequence', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_component_id'], ['product_component.id'], name=op.f('fk_product_component_data_product_component_id_product_component')),
    sa.ForeignKeyConstraint(['product_custom_field_id'], ['product_custom_field.id'], name=op.f('fk_product_component_data_product_custom_field_id_product_custom_field')),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_product_component_data_product_id_product')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_component_data'))
    )
    op.create_table('product_components',
    sa.Column('product_component_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_component_id'], ['product_component.id'], name=op.f('fk_product_components_product_component_id_product_component')),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_product_components_product_id_product')),
    sa.PrimaryKeyConstraint('product_component_id', 'product_id', name=op.f('pk_product_components'))
    )
    op.create_table('product_custom_fields',
    sa.Column('product_custom_field_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_custom_field_id'], ['product_custom_field.id'], name=op.f('fk_product_custom_fields_product_custom_field_id_product_custom_field')),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_product_custom_fields_product_id_product')),
    sa.PrimaryKeyConstraint('product_custom_field_id', 'product_id', name=op.f('pk_product_custom_fields'))
    )
    op.create_table('product_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_product_data_product_id_product')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_data'))
    )
    op.create_table('product_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=225), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('sequence', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_product_image_product_id_product')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product_image'))
    )
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('promotion_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name=op.f('fk_products_product_id_product')),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotion.id'], name=op.f('fk_products_promotion_id_promotion')),
    sa.PrimaryKeyConstraint('product_id', 'promotion_id', name=op.f('pk_products'))
    )
    op.create_table('orders',
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['card.id'], name=op.f('fk_orders_cart_id_card')),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name=op.f('fk_orders_order_id_order')),
    sa.PrimaryKeyConstraint('cart_id', 'order_id', name=op.f('pk_orders'))
    )
    op.create_table('product_components_data',
    sa.Column('product_component_data_id', sa.Integer(), nullable=False),
    sa.Column('product_data_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_component_data_id'], ['product_component_data.id'], name=op.f('fk_product_components_data_product_component_data_id_product_component_data')),
    sa.ForeignKeyConstraint(['product_data_id'], ['product_data.id'], name=op.f('fk_product_components_data_product_data_id_product_data')),
    sa.PrimaryKeyConstraint('product_component_data_id', 'product_data_id', name=op.f('pk_product_components_data'))
    )
    op.create_table('product_images',
    sa.Column('product_image_id', sa.Integer(), nullable=False),
    sa.Column('product_component_data_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_component_data_id'], ['product_component_data.id'], name=op.f('fk_product_images_product_component_data_id_product_component_data')),
    sa.ForeignKeyConstraint(['product_image_id'], ['product_image.id'], name=op.f('fk_product_images_product_image_id_product_image')),
    sa.PrimaryKeyConstraint('product_image_id', 'product_component_data_id', name=op.f('pk_product_images'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_images')
    op.drop_table('product_components_data')
    op.drop_table('orders')
    op.drop_table('products')
    op.drop_table('product_image')
    op.drop_table('product_data')
    op.drop_table('product_custom_fields')
    op.drop_table('product_components')
    op.drop_table('product_component_data')
    op.drop_table('product_categories')
    op.drop_table('order')
    op.drop_table('coupons')
    op.drop_table('active_codes_for_sel')
    op.drop_table('active_codes_for_custmr')
    op.drop_table('promotions')
    op.drop_table('product')
    op.drop_table('coupon')
    op.drop_table('seller')
    op.drop_table('promotion')
    op.drop_table('customer')
    op.drop_table('product_custom_field')
    op.drop_table('product_component')
    op.drop_table('product_category')
    op.drop_table('customer_avatar')
    op.drop_table('currency')
    op.drop_table('company_logo')
    op.drop_table('card')
    # ### end Alembic commands ###