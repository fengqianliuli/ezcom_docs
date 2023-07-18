
.. _program_listing_file_include_ezcom_node.h:

Program Listing for File node.h
===============================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_node.h>` (``include/ezcom/node.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   #include "types.h"
   
   namespace holosar {
   namespace ezcom {
   
   class Node {
    public:
     Node() = default;
     virtual ~Node() = default;
   
    protected:
     NodeType node_type_;
     CommMode comm_mode_;
     TransportType transport_type_;
   };
   
   }  // namespace ezcom
   }  // namespace holosar
   
