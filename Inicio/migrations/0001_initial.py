# Generated by Django 4.0.4 on 2022-06-02 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False, verbose_name='ID de la categoria')),
                ('nombreCat', models.CharField(max_length=30, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('idComuna', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de comuna')),
                ('nombreCom', models.CharField(max_length=40, verbose_name='Nombre comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('idMarca', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la marca')),
                ('nombreMarca', models.CharField(max_length=30, verbose_name='Nombre de la marca')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProd',
            fields=[
                ('idTiporod', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del tipo producto')),
                ('nombreTipoProd', models.CharField(max_length=60, verbose_name='ID del tipo producto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('idTipoUsuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del tipo usuario')),
                ('nombreTipo', models.CharField(max_length=30, verbose_name='Nombre del tipo de usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Username del usuario')),
                ('contrasennia', models.CharField(max_length=30, verbose_name='Contraseña del usuario')),
                ('nombre', models.CharField(max_length=60, verbose_name='Nombre del usuario')),
                ('apellido', models.CharField(max_length=60, verbose_name='Apellido del usuario')),
                ('email', models.CharField(max_length=150, verbose_name='Email del usuario')),
                ('tipousuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.tipousuario')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idVenta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de venta')),
                ('fechaVenta', models.DateField(verbose_name='Id de venta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('idRegion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de region')),
                ('nombreReg', models.CharField(max_length=40, verbose_name='Nombre region')),
                ('comuna', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inicio.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del Producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name='Nombre del Producto')),
                ('precioProducto', models.IntegerField(verbose_name='Precio del Producto')),
                ('especificacionProd', models.CharField(max_length=900, verbose_name='Especificaciones del Producto')),
                ('stockProd', models.IntegerField(verbose_name='Stock del Producto')),
                ('imagenProd', models.ImageField(null=True, upload_to='productos', verbose_name='Imagen del Producto')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.marca')),
                ('tipoprod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.tipoprod')),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('idModelo', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del modelo')),
                ('nombreModelo', models.CharField(max_length=30, verbose_name='Nombre del modelo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('idDireccion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de direccion')),
                ('descripcionDir', models.TextField(verbose_name='Descripcion direccion')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inicio.region')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('idDetalle', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del detalle')),
                ('cantidad', models.IntegerField(verbose_name='Cantidad')),
                ('subTotal', models.IntegerField(verbose_name='Subtotal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inicio.venta')),
            ],
        ),
    ]
