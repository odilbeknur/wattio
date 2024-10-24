-- Adminer 4.8.1 PostgreSQL 16.3 dump

INSERT INTO "auth_permission" ("id", "name", "content_type_id", "codename") VALUES
(1,	'Can add log entry',	1,	'add_logentry'),
(2,	'Can change log entry',	1,	'change_logentry'),
(3,	'Can delete log entry',	1,	'delete_logentry'),
(4,	'Can view log entry',	1,	'view_logentry'),
(5,	'Can add permission',	2,	'add_permission'),
(6,	'Can change permission',	2,	'change_permission'),
(7,	'Can delete permission',	2,	'delete_permission'),
(8,	'Can view permission',	2,	'view_permission'),
(9,	'Can add group',	3,	'add_group'),
(10,	'Can change group',	3,	'change_group'),
(11,	'Can delete group',	3,	'delete_group'),
(12,	'Can view group',	3,	'view_group'),
(13,	'Can add user',	4,	'add_user'),
(14,	'Can change user',	4,	'change_user'),
(15,	'Can delete user',	4,	'delete_user'),
(16,	'Can view user',	4,	'view_user'),
(17,	'Can add content type',	5,	'add_contenttype'),
(18,	'Can change content type',	5,	'change_contenttype'),
(19,	'Can delete content type',	5,	'delete_contenttype'),
(20,	'Can view content type',	5,	'view_contenttype'),
(21,	'Can add session',	6,	'add_session'),
(22,	'Can change session',	6,	'change_session'),
(23,	'Can delete session',	6,	'delete_session'),
(24,	'Can view session',	6,	'view_session'),
(25,	'Can add Станция',	7,	'add_plant'),
(26,	'Can change Станция',	7,	'change_plant'),
(27,	'Can delete Станция',	7,	'delete_plant'),
(28,	'Can view Станция',	7,	'view_plant'),
(29,	'Can add Инвертор',	8,	'add_inverter'),
(30,	'Can change Инвертор',	8,	'change_inverter'),
(31,	'Can delete Инвертор',	8,	'delete_inverter'),
(32,	'Can view Инвертор',	8,	'view_inverter');



INSERT INTO "django_migrations" ("id", "app", "name", "applied") VALUES
(1,	'contenttypes',	'0001_initial',	'2024-10-23 10:50:15.381801+00'),
(2,	'auth',	'0001_initial',	'2024-10-23 10:50:15.459063+00'),
(3,	'admin',	'0001_initial',	'2024-10-23 10:50:15.479622+00'),
(4,	'admin',	'0002_logentry_remove_auto_add',	'2024-10-23 10:50:15.483715+00'),
(5,	'admin',	'0003_logentry_add_action_flag_choices',	'2024-10-23 10:50:15.488222+00'),
(6,	'contenttypes',	'0002_remove_content_type_name',	'2024-10-23 10:50:15.496656+00'),
(7,	'auth',	'0002_alter_permission_name_max_length',	'2024-10-23 10:50:15.501421+00'),
(8,	'auth',	'0003_alter_user_email_max_length',	'2024-10-23 10:50:15.505511+00'),
(9,	'auth',	'0004_alter_user_username_opts',	'2024-10-23 10:50:15.509941+00'),
(10,	'auth',	'0005_alter_user_last_login_null',	'2024-10-23 10:50:15.514285+00'),
(11,	'auth',	'0006_require_contenttypes_0002',	'2024-10-23 10:50:15.516055+00'),
(12,	'auth',	'0007_alter_validators_add_error_messages',	'2024-10-23 10:50:15.520036+00'),
(13,	'auth',	'0008_alter_user_username_max_length',	'2024-10-23 10:50:15.528209+00'),
(14,	'auth',	'0009_alter_user_last_name_max_length',	'2024-10-23 10:50:15.532322+00'),
(15,	'auth',	'0010_alter_group_name_max_length',	'2024-10-23 10:50:15.538983+00'),
(16,	'auth',	'0011_update_proxy_permissions',	'2024-10-23 10:50:15.54282+00'),
(17,	'auth',	'0012_alter_user_first_name_max_length',	'2024-10-23 10:50:15.547608+00'),
(18,	'sessions',	'0001_initial',	'2024-10-23 10:50:15.563715+00'),
(19,	'wattio',	'0001_initial',	'2024-10-23 10:50:15.581104+00'),
(20,	'wattio',	'0002_inverter_name',	'2024-10-23 10:50:15.583585+00'),
(21,	'wattio',	'0003_plant_latitude_plant_longitude_plant_power_plant_utc_and_more',	'2024-10-23 10:50:15.627856+00'),
(22,	'wattio',	'0004_remove_plant_wattio_plan_name_66835c_idx_and_more',	'2024-10-23 10:50:15.644706+00'),
(23,	'wattio',	'0005_rename_plant_image_plant_image_and_more',	'2024-10-23 10:50:15.648948+00'),
(24,	'wattio',	'0006_alter_plant_address_alter_plant_image',	'2024-10-23 10:50:15.652532+00'),
(25,	'wattio',	'0007_alter_plant_address',	'2024-10-23 10:50:15.66731+00'),
(26,	'wattio',	'0008_plant_inverter_count',	'2024-10-23 10:50:15.670588+00'),
(27,	'wattio',	'0009_alter_inverter_plant',	'2024-10-23 10:50:15.67353+00');



INSERT INTO "wattio_inverter" ("id", "serial", "color", "plant_id", "name", "installation_date") VALUES
(1,	'XKK9CLS03V',	'#008FFB',	1,	'growatt',	NULL),
(2,	'2049-56500140D',	'#FEB019',	1,	'solax',	NULL),
(3,	'LJJ8CGA017',	'#008FFB',	2,	'growatt',	NULL),
(4,	'TASH_TTC_INV_1',	'#008FFB',	3,	'growatt',	NULL),
(5,	'TASH_TTC_INV_2',	'#008FFB',	3,	'growatt',	NULL),
(6,	'TASH_TTC_INV_3',	'#008FFB',	3,	'growatt',	NULL),
(7,	'TASH_TTC_INV_4',	'#008FFB',	3,	'growatt',	NULL),
(8,	'TASH_TTC_INV_5',	'#008FFB',	3,	'growatt',	NULL),
(9,	'TASH_TTC_INV_6',	'#008FFB',	3,	'growatt',	NULL),
(10,	'TASH_TTC_INV_7',	'#FEB019',	3,	'growatt',	NULL),
(11,	'TASH_TTC_INV_8',	'#008FFB',	3,	'growatt',	NULL),
(12,	'SIR_TPP_INV_1',	'#008FFB',	4,	'growatt',	NULL),
(13,	'SIR_TPP_INV_2',	'#008FFB',	4,	'growatt',	NULL),
(14,	'SIR_TPP_INV_3',	'#008FFB',	4,	'growatt',	NULL),
(15,	'SIR_TPP_INV_4',	'#FEB019',	4,	'growatt',	NULL),
(16,	'SIR_TPP_INV_5',	'#008FFB',	4,	'growatt',	NULL),
(17,	'SIR_TPP_INV_6',	'#008FFB',	4,	'growatt',	NULL),
(18,	'SIR_TPP_INV_7',	'#008FFB',	4,	'growatt',	NULL),
(19,	'SIR_TPP_INV_8',	'#008FFB',	4,	'growatt',	NULL),
(20,	'SIR_TPP_INV_9',	'#008FFB',	4,	'growatt',	NULL),
(21,	'SIR_TPP_INV_10',	'#008FFB',	4,	'growatt',	NULL),
(22,	'SIR_TPP_INV_11',	'#008FFB',	4,	'growatt',	NULL),
(23,	'SIR_TPP_INV_12',	'#008FFB',	4,	'growatt',	NULL),
(24,	'SIR_TPP_INV_13',	'#008FFB',	4,	'growatt',	NULL),
(25,	'SIR_TPP_INV_14',	'#008FFB',	4,	'growatt',	NULL),
(26,	'SIR_TPP_INV_15',	'#008FFB',	4,	'growatt',	NULL),
(27,	'SIR_TPP_INV_16',	'#008FFB',	4,	'growatt',	NULL),
(28,	'MUB_TPP_INV_1',	'#FEB019',	3,	'growatt',	NULL),
(29,	'MUB_TPP_INV_2',	'#008FFB',	3,	'growatt',	NULL),
(30,	'MUB_TPP_INV_3',	'#008FFB',	4,	'growatt',	NULL),
(31,	'MUB_TPP_INV_4',	'#008FFB',	4,	'growatt',	NULL),
(32,	'MUB_TPP_INV_5',	'#008FFB',	4,	'growatt',	NULL),
(33,	'MUB_TPP_INV_6',	'#FEB019',	4,	'growatt',	NULL),
(34,	'MUB_TPP_INV_7',	'#008FFB',	4,	'growatt',	NULL),
(35,	'MUB_TPP_INV_8',	'#008FFB',	4,	'growatt',	NULL),
(36,	'MUB_TPP_INV_9',	'#008FFB',	4,	'growatt',	NULL),
(37,	'MUB_TPP_INV_10',	'#008FFB',	4,	'growatt',	NULL),




INSERT INTO "wattio_plant" ("id", "name", "latitude", "longitude", "power", "address", "city", "country", "image", "timezone", "inverter_count") VALUES
(1,	'АО ТЭС',	41.2819245,	69.265,	74.00,	'JSC_TPP',	'Ташкент',	'Узбекистан',	'plants/ies_UGnKiJ5_kJgMvJc_tYwdy7P.png',	'5',	2),
(2,	'Узэнергосозлаш',	41.2819245,	69.2082656,	30.00,	'SOZLASH_MAIN',	'Ташкент',	'Узбекистан',	'plants/16f9226f-a6eb-6cd6-8f41-84925ff0d7fc_news__DFLdSZM.jpg',	'5',	1),
(3,	'Ташкентская ТЭЦ',	41.2745905,	69.6,	530.60,	'TASHKENT_TTC',	'Ташкент',	'Узбекистан',	'plants/NzHMRHYPVXM8ZKshSVA3Vnj9Q6zhhvXF_low.jpg',	'5',	8),
(4,	'Сырдарьинская ТЭС',	40.2313035,	69.0914677,	1924.10,	'SIRDARYA_TPP',	'Сырдарья',	'Узбекистан',	'plants/5dbec7314ae54d9e3f847.png',	'5',	16);
(5,	'Мубарекская ТЭЦ',	39.181493023042904,	65.29066739434548,	1220.00,	'MUBAREK_TPP',	'Мубарек',	'Узбекистан',	'plants/5dbec7314ae54d9e3f847.png',	'5',	10);

ALTER TABLE ONLY "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;
ALTER TABLE ONLY "public"."auth_group_permissions" ADD CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;

ALTER TABLE ONLY "public"."auth_permission" ADD CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;

ALTER TABLE ONLY "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY (group_id) REFERENCES auth_group(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;
ALTER TABLE ONLY "public"."auth_user_groups" ADD CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;

ALTER TABLE ONLY "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY (permission_id) REFERENCES auth_permission(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;
ALTER TABLE ONLY "public"."auth_user_user_permissions" ADD CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;

ALTER TABLE ONLY "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY (content_type_id) REFERENCES django_content_type(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;
ALTER TABLE ONLY "public"."django_admin_log" ADD CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY (user_id) REFERENCES auth_user(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;

ALTER TABLE ONLY "public"."wattio_inverter" ADD CONSTRAINT "wattio_inverter_plant_id_04b6e527_fk_wattio_plant_id" FOREIGN KEY (plant_id) REFERENCES wattio_plant(id) DEFERRABLE INITIALLY DEFERRED DEFERRABLE;

-- 2024-10-24 06:57:23.90025+00
