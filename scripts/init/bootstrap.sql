--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: hh-expo; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA "parser";


GRANT USAGE ON SCHEMA "parser" TO role_rw;
GRANT USAGE ON SCHEMA "parser" TO role_ro;

CREATE USER "parser_user" UNENCRYPTED PASSWORD '1234';
GRANT role_rw TO "parser_user";
ALTER USER "parser_user" SET search_path = 'parser';

SET search_path = 'parser';

CREATE SEQUENCE media_file_seq;
GRANT SELECT, UPDATE ON media_file_seq TO role_rw;

ALTER SCHEMA "parser" OWNER TO postgres;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;

BEGIN;
CREATE TABLE "admin_tools_menu_bookmark" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "url" varchar(255) NOT NULL,
    "title" varchar(255) NOT NULL
)
;
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE "admin_tools_menu_bookmark" ADD CONSTRAINT "user_id_refs_id_1dc7bd98" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "admin_tools_menu_bookmark_user_id" ON "admin_tools_menu_bookmark" ("user_id");

GRANT SELECT, UPDATE, INSERT, DELETE ON admin_tools_menu_bookmark TO role_rw;
GRANT SELECT ON admin_tools_menu_bookmark TO role_ro;
GRANT SELECT, UPDATE ON admin_tools_menu_bookmark_id_seq TO role_rw;

COMMIT;


BEGIN;
CREATE TABLE "admin_tools_dashboard_preferences" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "data" text NOT NULL,
    "dashboard_id" varchar(100) NOT NULL,
    UNIQUE ("user_id", "dashboard_id")
)
;
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE "admin_tools_dashboard_preferences" ADD CONSTRAINT "user_id_refs_id_23127ba7" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "admin_tools_dashboard_preferences_user_id" ON "admin_tools_dashboard_preferences" ("user_id");

GRANT SELECT, UPDATE, INSERT, DELETE ON admin_tools_dashboard_preferences TO role_rw;
GRANT SELECT ON admin_tools_dashboard_preferences TO role_ro;
GRANT SELECT, UPDATE ON admin_tools_dashboard_preferences_id_seq TO role_rw;

COMMIT;


BEGIN;
CREATE TABLE "auth_permission" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "content_type_id" integer NOT NULL,
    "codename" varchar(100) NOT NULL,
    UNIQUE ("content_type_id", "codename")
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON auth_permission TO role_rw;
GRANT SELECT ON auth_permission TO role_ro;
GRANT SELECT, UPDATE ON auth_permission_id_seq TO role_rw;

CREATE TABLE "auth_group_permissions" (
    "id" serial NOT NULL PRIMARY KEY,
    "group_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("group_id", "permission_id")
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON auth_group_permissions TO role_rw;
GRANT SELECT ON auth_group_permissions TO role_ro;
GRANT SELECT, UPDATE ON auth_group_permissions_id_seq TO role_rw;


CREATE TABLE "auth_group" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(80) NOT NULL UNIQUE
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON auth_group TO role_rw;
GRANT SELECT ON auth_group TO role_ro;
GRANT SELECT, UPDATE ON auth_group_id_seq TO role_rw;

ALTER TABLE "auth_group_permissions" ADD CONSTRAINT "group_id_refs_id_f4b32aac" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE TABLE "auth_user_groups" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("user_id", "group_id")
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON auth_user_groups TO role_rw;
GRANT SELECT ON auth_user_groups TO role_ro;
GRANT SELECT, UPDATE ON auth_user_groups_id_seq TO role_rw;

CREATE TABLE "auth_user_user_permissions" (
    "id" serial NOT NULL PRIMARY KEY,
    "user_id" integer NOT NULL,
    "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("user_id", "permission_id")
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON auth_user_user_permissions TO role_rw;
GRANT SELECT ON auth_user_user_permissions TO role_ro;
GRANT SELECT, UPDATE ON auth_user_user_permissions_id_seq TO role_rw;

CREATE TABLE "auth_user" (
    "id" serial NOT NULL PRIMARY KEY,
    "password" varchar(128) NOT NULL,
    "last_login" timestamp with time zone NOT NULL,
    "is_superuser" boolean NOT NULL,
    "username" varchar(30) NOT NULL UNIQUE,
    "first_name" varchar(30) NOT NULL,
    "last_name" varchar(30) NOT NULL,
    "email" varchar(75) NOT NULL,
    "is_staff" boolean NOT NULL,
    "is_active" boolean NOT NULL,
    "date_joined" timestamp with time zone NOT NULL
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON auth_user TO role_rw;
GRANT SELECT ON auth_user TO role_ro;
GRANT SELECT, UPDATE ON auth_user_id_seq TO role_rw;

ALTER TABLE "auth_user_groups" ADD CONSTRAINT "user_id_refs_id_40c41112" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "auth_user_user_permissions" ADD CONSTRAINT "user_id_refs_id_4dc23c39" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE "auth_permission" ADD CONSTRAINT "content_type_id_refs_id_d043b34a" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "auth_permission_content_type_id" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_group_id" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_group_name_like" ON "auth_group" ("name" varchar_pattern_ops);
CREATE INDEX "auth_user_groups_user_id" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_user_id" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "auth_user_username_like" ON "auth_user" ("username" varchar_pattern_ops);

COMMIT;

BEGIN;
CREATE TABLE "django_content_type" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(100) NOT NULL,
    "app_label" varchar(100) NOT NULL,
    "model" varchar(100) NOT NULL,
    UNIQUE ("app_label", "model")
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON django_content_type TO role_rw;
GRANT SELECT ON django_content_type TO role_ro;
GRANT SELECT, UPDATE ON django_content_type_id_seq TO role_rw;

COMMIT;

BEGIN;
CREATE TABLE "django_session" (
    "session_key" varchar(40) NOT NULL PRIMARY KEY,
    "session_data" text NOT NULL,
    "expire_date" timestamp with time zone NOT NULL
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON django_session TO role_rw;
GRANT SELECT ON django_session TO role_ro;

CREATE INDEX "django_session_session_key_like" ON "django_session" ("session_key" varchar_pattern_ops);
CREATE INDEX "django_session_expire_date" ON "django_session" ("expire_date");

COMMIT;

BEGIN;
CREATE TABLE "django_admin_log" (
    "id" serial NOT NULL PRIMARY KEY,
    "action_time" timestamp with time zone NOT NULL,
    "user_id" integer NOT NULL,
    "content_type_id" integer,
    "object_id" text,
    "object_repr" varchar(200) NOT NULL,
    "action_flag" smallint CHECK ("action_flag" >= 0) NOT NULL,
    "change_message" text NOT NULL
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON django_admin_log TO role_rw;
GRANT SELECT ON django_admin_log TO role_ro;
GRANT SELECT, UPDATE ON django_admin_log_id_seq TO role_rw;

-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE "django_admin_log" ADD CONSTRAINT "content_type_id_refs_id_93d2d1f8" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED;
-- ALTER TABLE "django_admin_log" ADD CONSTRAINT "user_id_refs_id_c0d12874" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "django_admin_log_user_id" ON "django_admin_log" ("user_id");
CREATE INDEX "django_admin_log_content_type_id" ON "django_admin_log" ("content_type_id");

COMMIT;

BEGIN;
CREATE TABLE "django_site" (
    "id" serial NOT NULL PRIMARY KEY,
    "domain" varchar(100) NOT NULL,
    "name" varchar(50) NOT NULL
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON django_site TO role_rw;
GRANT SELECT ON django_site TO role_ro;
GRANT SELECT, UPDATE ON django_site_id_seq TO role_rw;

COMMIT;

BEGIN;
CREATE TABLE "webdav_mediafilesequence" (
    "id" serial NOT NULL PRIMARY KEY
)
;
GRANT SELECT, UPDATE, INSERT, DELETE ON webdav_mediafilesequence TO role_rw;
GRANT SELECT ON webdav_mediafilesequence TO role_ro;
GRANT SELECT, UPDATE ON webdav_mediafilesequence_id_seq TO role_rw;

COMMIT;
