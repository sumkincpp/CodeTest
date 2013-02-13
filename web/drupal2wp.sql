# Drupal to wordpress migration
# http://9seeds.com/news/drupal-to-wordpress-migration

TRUNCATE TABLE wpblog.wp_comments;
TRUNCATE TABLE wpblog.wp_links;
TRUNCATE TABLE wpblog.wp_postmeta;
TRUNCATE TABLE wpblog.wp_posts;
TRUNCATE TABLE wpblog.wp_term_relationships;
TRUNCATE TABLE wpblog.wp_term_taxonomy;
TRUNCATE TABLE wpblog.wp_terms;

INSERT INTO wpblog.wp_terms (term_id, `name`, slug, term_group)
SELECT
 d.tid, d.name, REPLACE(LOWER(d.name), ' ', '_'), 0
FROM qosys.drbl_taxonomy_term_data d
INNER JOIN qosys.drbl_taxonomy_term_hierarchy h
 USING(tid)
 
 
INSERT INTO wpblog.wp_term_taxonomy (term_id, taxonomy, description, parent)
SELECT
 d.tid `term_id`,
 IF(txv.name="tags","post_tag",txv.name) `taxonomy`,
 d.description `description`,
 h.parent `parent`
FROM qosys.drbl_taxonomy_term_data d
INNER JOIN qosys.drbl_taxonomy_term_hierarchy h
 USING(tid)
LEFT OUTER JOIN qosys.drbl_taxonomy_vocabulary txv
 ON txv.vid = d.vid;
 
INSERT INTO wpblog.wp_posts (id, post_date, post_content, post_title, post_excerpt, post_modified, post_type, `post_status`)
SELECT DISTINCT
 n.nid `id`,
 FROM_UNIXTIME(n.created) `post_date`,
 fb.body_value `post_content`,
 n.title `post_title`,
 fb.body_summary `post_excerpt`,
 FROM_UNIXTIME(n.changed) `post_modified`,
 n.TYPE `post_type`,
 IF(n.STATUS = 1, 'publish', 'private') `post_status`
FROM qosys.drbl_node n
INNER JOIN qosys.drbl_node_revision r
 USING(vid)
LEFT OUTER JOIN qosys.drbl_field_data_body fb
 ON fb.entity_id = n.nid
WHERE n.TYPE IN ('page', 'story')

UPDATE wpblog.wp_posts SET post_type='post' WHERE post_type='story';

INSERT INTO wpblog.wp_term_relationships (object_id, term_taxonomy_id)
SELECT nid, tid FROM qosys.drbl_taxonomy_index;
--
INSERT INTO wpblog.wp_term_relationships (object_id, term_taxonomy_id)
SELECT nid, tx.term_taxonomy_id
FROM qosys.drbl_taxonomy_index
INNER JOIN wpblog.wp_term_taxonomy tx ON tx.term_id = tid


UPDATE wpblog.wp_term_taxonomy tt
SET `count` = (
 SELECT COUNT(tr.object_id)
 FROM wpblog.wp_term_relationships tr
 WHERE tr.term_taxonomy_id = tt.term_taxonomy_id);
 
INSERT INTO wpblog.wp_comments (comment_post_ID, comment_date, comment_content, comment_parent, comment_author, comment_author_email, comment_author_url, comment_approved)
SELECT nid, FROM_UNIXTIME(created), subject, pid, name, mail, homepage, STATUS FROM qosys.drbl_comment

USE wpblog;
UPDATE `wp_posts` SET `comment_count` = (SELECT COUNT(`comment_post_id`) FROM `wp_comments` WHERE `wp_posts`.`id` = `wp_comments`.`comment_post_id`);

UPDATE wpblog.wp_posts SET post_content = REPLACE(post_content, '"/files/', '"/wp-content/uploads/');