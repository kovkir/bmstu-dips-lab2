--
-- PostgreSQL database dump
--

-- Dumped from database version 16.0
-- Dumped by pg_dump version 16.0

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
-- Name: airports; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.airports (
    id integer NOT NULL,
    name character varying(255),
    city character varying(255),
    country character varying(255)
);


ALTER TABLE public.airports OWNER TO postgres;

--
-- Name: airports_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.airports_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.airports_id_seq OWNER TO postgres;

--
-- Name: airports_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.airports_id_seq OWNED BY public.airports.id;


--
-- Name: flights; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.flights (
    id integer NOT NULL,
    flight_number character varying(20) NOT NULL,
    price integer NOT NULL,
    datetime timestamp with time zone NOT NULL,
    from_airport_id integer,
    to_airport_id integer
);


ALTER TABLE public.flights OWNER TO postgres;

--
-- Name: flights_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.flights_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.flights_id_seq OWNER TO postgres;

--
-- Name: flights_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.flights_id_seq OWNED BY public.flights.id;


--
-- Name: airports id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.airports ALTER COLUMN id SET DEFAULT nextval('public.airports_id_seq'::regclass);


--
-- Name: flights id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flights ALTER COLUMN id SET DEFAULT nextval('public.flights_id_seq'::regclass);


--
-- Data for Name: airports; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.airports (id, name, city, country) FROM stdin;
1	Шереметьево	Москва	Россия
2	Пулково	Санкт-Петербург	Россия
\.


--
-- Data for Name: flights; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.flights (id, flight_number, price, datetime, from_airport_id, to_airport_id) FROM stdin;
1	AFL031	1500	2021-10-08 20:00:00+00	2	1
\.


--
-- Name: airports_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.airports_id_seq', 2, true);


--
-- Name: flights_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.flights_id_seq', 1, true);


--
-- Name: airports airports_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.airports
    ADD CONSTRAINT airports_pkey PRIMARY KEY (id);


--
-- Name: flights flights_flight_number_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flights
    ADD CONSTRAINT flights_flight_number_key UNIQUE (flight_number);


--
-- Name: flights flights_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flights
    ADD CONSTRAINT flights_pkey PRIMARY KEY (id);


--
-- Name: ix_airports_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_airports_id ON public.airports USING btree (id);


--
-- Name: ix_flights_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_flights_id ON public.flights USING btree (id);


--
-- Name: flights flights_from_airport_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flights
    ADD CONSTRAINT flights_from_airport_id_fkey FOREIGN KEY (from_airport_id) REFERENCES public.airports(id);


--
-- Name: flights flights_to_airport_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.flights
    ADD CONSTRAINT flights_to_airport_id_fkey FOREIGN KEY (to_airport_id) REFERENCES public.airports(id);


--
-- PostgreSQL database dump complete
--

