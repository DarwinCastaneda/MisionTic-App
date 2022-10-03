# Generated by Django 4.1.1 on 2022-10-01 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermero',
            fields=[
                ('id_enfermero', models.AutoField(primary_key=True, serialize=False)),
                ('especialidad', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='HistoriaClinica',
            fields=[
                ('id_historiaClinica', models.AutoField(primary_key=True, serialize=False)),
                ('motivo_consulta', models.CharField(max_length=100)),
                ('enfermedad_actual', models.CharField(max_length=100)),
                ('fecha_consulta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id_medico', models.AutoField(primary_key=True, serialize=False)),
                ('tarjeta_profesional', models.CharField(max_length=20)),
                ('especialialidad', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id_tipoUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('rol', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id_signos_vitales', models.AutoField(primary_key=True, serialize=False)),
                ('oximetria', models.CharField(max_length=20)),
                ('frecuencia_respiratoria', models.CharField(max_length=20)),
                ('frecuencia_cardiaca', models.CharField(max_length=20)),
                ('temperatura', models.CharField(max_length=10)),
                ('presion_arterial', models.CharField(max_length=20)),
                ('glicemias', models.CharField(max_length=20)),
                ('fecha_hora', models.DateTimeField()),
                ('id_historiaClinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signos', to='hosApp.historiaclinica')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id_paciente', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=15)),
                ('ciudad', models.CharField(max_length=35)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('id_enfermero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='hosApp.enfermero')),
                ('id_historiaClinica', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='hosApp.historiaclinica')),
                ('id_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='hosApp.medico')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id_familar', models.AutoField(primary_key=True, serialize=False)),
                ('correo', models.EmailField(max_length=35)),
                ('parentesco', models.CharField(max_length=10)),
                ('id_paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='enfermero', to='hosApp.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id_diagnostico', models.AutoField(primary_key=True, serialize=False)),
                ('sugerencia', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('id_historiaClinica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diagnostico', to='hosApp.historiaclinica')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=15, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('celular', models.CharField(max_length=10, verbose_name='Celular')),
                ('correo', models.EmailField(max_length=30, verbose_name='Correo')),
                ('genero', models.CharField(max_length=2, verbose_name='Genero')),
                ('edad', models.CharField(max_length=2, verbose_name='Edad')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('id_enfermero', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='hosApp.enfermero')),
                ('id_familiar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='hosApp.familiar')),
                ('id_medico', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='hosApp.medico')),
                ('id_paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='hosApp.paciente')),
                ('id_tipoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to='hosApp.tipousuario')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]