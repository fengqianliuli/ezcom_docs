
.. _program_listing_file_include_ezcom_publisher.h:

Program Listing for File publisher.h
====================================

|exhale_lsh| :ref:`Return to documentation for file <file_include_ezcom_publisher.h>` (``include/ezcom/publisher.h``)

.. |exhale_lsh| unicode:: U+021B0 .. UPWARDS ARROW WITH TIP LEFTWARDS

.. code-block:: cpp

   
   #pragma once
   
   #include <string>
   
   #include "message.h"
   #include "node.h"
   
   namespace holosar {
   namespace ezcom {
   
   class Publisher : public Node {
    public:
     Publisher() = default;
     virtual ~Publisher() = default;
     virtual void Bind(const std::string& addr) = 0;
     virtual void Publish(const std::shared_ptr<Message>& msg,
                          const std::string& topic = "default_topic") = 0;
   };
   
   }  // namespace ezcom
   }  // namespace holosar
