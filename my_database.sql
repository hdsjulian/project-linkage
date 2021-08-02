--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: coins; Type: TABLE; Schema: public; Owner: xktqolizmrwyjt
--

CREATE TABLE public.coins (
    id integer NOT NULL,
    hash character varying
);


ALTER TABLE public.coins OWNER TO xktqolizmrwyjt;

--
-- Name: coins_id_seq; Type: SEQUENCE; Schema: public; Owner: xktqolizmrwyjt
--

CREATE SEQUENCE public.coins_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.coins_id_seq OWNER TO xktqolizmrwyjt;

--
-- Name: coins_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: xktqolizmrwyjt
--

ALTER SEQUENCE public.coins_id_seq OWNED BY public.coins.id;


--
-- Name: handovers; Type: TABLE; Schema: public; Owner: xktqolizmrwyjt
--

CREATE TABLE public.handovers (
    id integer NOT NULL,
    lat double precision,
    lon double precision,
    text text,
    "timestamp" integer,
    predecessor_id integer,
    recipient_id integer,
    giver_id integer
);


ALTER TABLE public.handovers OWNER TO xktqolizmrwyjt;

--
-- Name: handovers_id_seq; Type: SEQUENCE; Schema: public; Owner: xktqolizmrwyjt
--

CREATE SEQUENCE public.handovers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.handovers_id_seq OWNER TO xktqolizmrwyjt;

--
-- Name: handovers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: xktqolizmrwyjt
--

ALTER SEQUENCE public.handovers_id_seq OWNED BY public.handovers.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: xktqolizmrwyjt
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying,
    hashed_password character varying,
    name character varying
);


ALTER TABLE public.users OWNER TO xktqolizmrwyjt;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: xktqolizmrwyjt
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO xktqolizmrwyjt;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: xktqolizmrwyjt
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: coins id; Type: DEFAULT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.coins ALTER COLUMN id SET DEFAULT nextval('public.coins_id_seq'::regclass);


--
-- Name: handovers id; Type: DEFAULT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.handovers ALTER COLUMN id SET DEFAULT nextval('public.handovers_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: coins; Type: TABLE DATA; Schema: public; Owner: xktqolizmrwyjt
--

COPY public.coins (id, hash) FROM stdin;
\.


--
-- Data for Name: handovers; Type: TABLE DATA; Schema: public; Owner: xktqolizmrwyjt
--

COPY public.handovers (id, lat, lon, text, "timestamp", predecessor_id, recipient_id, giver_id) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: xktqolizmrwyjt
--

COPY public.users (id, email, hashed_password, name) FROM stdin;
1	julian@phinn.de	awet151	Julian
\.


--
-- Name: coins_id_seq; Type: SEQUENCE SET; Schema: public; Owner: xktqolizmrwyjt
--

SELECT pg_catalog.setval('public.coins_id_seq', 1, false);


--
-- Name: handovers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: xktqolizmrwyjt
--

SELECT pg_catalog.setval('public.handovers_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: xktqolizmrwyjt
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: coins coins_hash_key; Type: CONSTRAINT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.coins
    ADD CONSTRAINT coins_hash_key UNIQUE (hash);


--
-- Name: coins coins_pkey; Type: CONSTRAINT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.coins
    ADD CONSTRAINT coins_pkey PRIMARY KEY (id);


--
-- Name: handovers handovers_pkey; Type: CONSTRAINT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.handovers
    ADD CONSTRAINT handovers_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_coins_id; Type: INDEX; Schema: public; Owner: xktqolizmrwyjt
--

CREATE INDEX ix_coins_id ON public.coins USING btree (id);


--
-- Name: ix_handovers_id; Type: INDEX; Schema: public; Owner: xktqolizmrwyjt
--

CREATE INDEX ix_handovers_id ON public.handovers USING btree (id);


--
-- Name: ix_handovers_timestamp; Type: INDEX; Schema: public; Owner: xktqolizmrwyjt
--

CREATE INDEX ix_handovers_timestamp ON public.handovers USING btree ("timestamp");


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: xktqolizmrwyjt
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: xktqolizmrwyjt
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: handovers handovers_giver_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.handovers
    ADD CONSTRAINT handovers_giver_id_fkey FOREIGN KEY (giver_id) REFERENCES public.users(id);


--
-- Name: handovers handovers_predecessor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.handovers
    ADD CONSTRAINT handovers_predecessor_id_fkey FOREIGN KEY (predecessor_id) REFERENCES public.handovers(id);


--
-- Name: handovers handovers_recipient_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: xktqolizmrwyjt
--

ALTER TABLE ONLY public.handovers
    ADD CONSTRAINT handovers_recipient_id_fkey FOREIGN KEY (recipient_id) REFERENCES public.users(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: xktqolizmrwyjt
--

REVOKE ALL ON SCHEMA public FROM postgres;
REVOKE ALL ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO xktqolizmrwyjt;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- Name: LANGUAGE plpgsql; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON LANGUAGE plpgsql TO xktqolizmrwyjt;


--
-- PostgreSQL database dump complete
--

